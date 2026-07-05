document.querySelectorAll("form").forEach(form => {

form.addEventListener("submit", function(e){

let preview = document.querySelector(".preview");

if(preview){

let confirmUpload = confirm("Upload another file?");

if(!confirmUpload){
e.preventDefault();
}

}

});

});