# 😊 Emotion Detection Using Facial Expressions

A real-time facial emotion recognition web application built using **Python**, **FastAPI**, **OpenCV**, and **DeepFace**. The application detects faces from uploaded images and videos, analyzes facial expressions using deep learning, and predicts the dominant emotion with visual annotations.

---

## 🚀 Features

* Real-time facial emotion recognition
* Emotion detection from images
* Emotion detection from videos
* Automatic face detection using OpenCV
* Deep learning-based emotion analysis with DeepFace
* User-friendly FastAPI web interface
* Displays detected emotion labels on faces
* Supports multiple faces in a single frame

---

## 🛠️ Technology Stack

### Programming Language

* Python

### Framework

* FastAPI

### Computer Vision

* OpenCV
* Haar Cascade Face Detector

### Deep Learning

* DeepFace
* TensorFlow / Keras

### Frontend

* HTML
* CSS
* JavaScript
* Jinja2 Templates

---

## 📂 Project Structure

```text
emotion_detection/
│
├── main.py
├── requirements.txt
│
├── static/
│   ├── css/
│   ├── js/
│   ├── uploads/
│   └── output/
│
├── templates/
│   ├── home.html
│   ├── image.html
│   ├── video.html
│   └── index.html
│
└── README.md
```

---

## ⚙️ How It Works

1. Upload an image or video.
2. OpenCV detects all faces.
3. Each detected face is passed to DeepFace.
4. DeepFace predicts the dominant emotion.
5. Bounding boxes and emotion labels are drawn.
6. The processed image or video is displayed to the user.

---

## 🎯 Detected Emotions

* Happy 😀
* Sad 😢
* Angry 😠
* Fear 😨
* Surprise 😲
* Disgust 🤢
* Neutral 😐

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/EmotionDetectionUsingFacialExpressions.git
```

Navigate to the project:

```bash
cd EmotionDetectionUsingFacialExpressions
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
uvicorn main:app --reload
```

Open your browser:

```
http://127.0.0.1:8000
```

---

## 📸 Application Modules

### 🖼️ Image Emotion Detection

* Upload an image.
* Detect faces.
* Predict emotions.
* Display annotated output.

### 🎥 Video Emotion Detection

* Upload a video.
* Analyze each frame.
* Detect emotions frame-by-frame.
* Generate an annotated output video.

---

## 📈 Project Highlights

* Built an end-to-end emotion recognition pipeline.
* Implemented face detection using OpenCV Haar Cascades.
* Used DeepFace for emotion classification with pretrained deep learning models.
* Developed a responsive web interface using FastAPI and Jinja2.
* Integrated image and video processing into a single application.

---

## 🔮 Future Improvements

* Live webcam emotion detection
* Emotion confidence visualization
* Face tracking for smoother video predictions
* Docker support
* Cloud deployment
* REST API documentation using Swagger

---

## 📚 Skills Demonstrated

* Python
* FastAPI
* OpenCV
* DeepFace
* TensorFlow
* Computer Vision
* Deep Learning
* Image Processing
* Video Processing
* Web Application Development

---

## 👩‍💻 Author

**Anjali**

Machine Learning • Deep Learning • Computer Vision • Data Engineering

If you found this project useful, consider giving it a ⭐ on GitHub.
