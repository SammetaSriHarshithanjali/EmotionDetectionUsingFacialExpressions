import os
import uuid
import cv2
import subprocess
from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from deepface import DeepFace

app = FastAPI()

# Create folders
os.makedirs("static/uploads", exist_ok=True)
os.makedirs("static/output", exist_ok=True)

# Mount static folder
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

# Face detection model
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# ================= HOME =================
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


# ================= IMAGE PAGE =================
@app.get("/image", response_class=HTMLResponse)
async def image_page(request: Request):
    return templates.TemplateResponse("image.html", {"request": request})


# ================= VIDEO PAGE =================
@app.get("/video", response_class=HTMLResponse)
async def video_page(request: Request):
    return templates.TemplateResponse("video.html", {"request": request})


# ================= IMAGE UPLOAD =================
@app.post("/upload-image/", response_class=HTMLResponse)
async def upload_image(request: Request, file: UploadFile = File(...)):

    unique_id = str(uuid.uuid4())

    input_path = f"static/uploads/{unique_id}.jpg"
    output_path = f"static/output/{unique_id}_output.jpg"

    with open(input_path, "wb") as buffer:
        buffer.write(await file.read())

    image = cv2.imread(input_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    for (x, y, w, h) in faces:
        face_roi = image[y:y+h, x:x+w]

        try:
            result = DeepFace.analyze(
                face_roi,
                actions=['emotion'],
                enforce_detection=False
            )

            emotion = result[0]['dominant_emotion']

            cv2.rectangle(image, (x,y), (x+w,y+h), (0,255,0), 2)
            cv2.putText(image, emotion, (x,y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9,
                        (0,255,0), 2)
        except:
            pass

    cv2.imwrite(output_path, image)

    return templates.TemplateResponse(
        "image.html",
        {
            "request": request,
            "input_image": f"/{input_path}?v={unique_id}",
            "output_image": f"/{output_path}?v={unique_id}"
        }
    )


# ================= VIDEO UPLOAD =================
@app.post("/upload-video/", response_class=HTMLResponse)
async def upload_video(request: Request, file: UploadFile = File(...)):

    unique_id = str(uuid.uuid4())

    input_path = f"static/uploads/{unique_id}.mp4"
    temp_output = f"static/output/{unique_id}_temp.avi"
    final_output = f"static/output/{unique_id}_output.mp4"

    # Save uploaded video
    with open(input_path, "wb") as buffer:
        buffer.write(await file.read())

    cap = cv2.VideoCapture(input_path)

    fps = cap.get(cv2.CAP_PROP_FPS)
    if fps == 0:
        fps = 25

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Temporary AVI file
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter(temp_output, fourcc, fps, (width, height))

    while True:

        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 5)

        for (x, y, w, h) in faces:

            face_roi = frame[y:y+h, x:x+w]

            try:
                result = DeepFace.analyze(
                    face_roi,
                    actions=['emotion'],
                    enforce_detection=False
                )

                emotion = result[0]['dominant_emotion']

                cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)

                cv2.putText(frame, emotion, (x,y-10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.9,
                            (0,255,0), 2)

            except:
                pass

        out.write(frame)

    cap.release()
    out.release()

    # Convert AVI → H264 MP4 using FFmpeg
    subprocess.run([
        "C:\\Users\\sriha\\AppData\\Local\\Microsoft\\WinGet\\Links\\ffmpeg.exe",
        "-y",
        "-i", temp_output,
        "-vcodec", "libx264",
        "-acodec", "aac",
        final_output
    ])

    return templates.TemplateResponse(
        "video.html",
        {
            "request": request,
            "input_video": f"/{input_path}?v={unique_id}",
            "output_video": f"/{final_output}?v={unique_id}"
        }
    )