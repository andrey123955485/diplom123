document.addEventListener('DOMContentLoaded', function() {
    const fileInput = document.getElementById('image');
    fileInput.addEventListener('change', function(event) {
        console.log("Файл выбран:", event.target.files[0]);
    });
});
