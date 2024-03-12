const canvas = document.getElementById("inputCanvas");
const ctx = canvas.getContext("2d");
const predictButton = document.getElementById("predictBtn");
const clearButton = document.getElementById("clearBtn");
const predictionDiv = document.getElementById("prediction");
const fileInput = document.getElementById("fileInput");
const uploadButton = document.getElementById("uploadBtn");

function initCanvas() {
    ctx.fillStyle = "white";
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.lineWidth = 5;
    ctx.lineCap = "round";
    ctx.strokeStyle = "black";
}

initCanvas();

let isDrawing = false;

canvas.addEventListener("mousedown", (e) => {
    isDrawing = true;
    ctx.beginPath();
    ctx.moveTo(e.offsetX, e.offsetY);
});

canvas.addEventListener("mousemove", (e) => {
    if (isDrawing) {
        ctx.lineTo(e.offsetX, e.offsetY);
        ctx.stroke();
    }
});

canvas.addEventListener("mouseup", () => isDrawing = false);
canvas.addEventListener("mouseout", () => isDrawing = false);

clearButton.addEventListener("click", () => {
   ctx.clearRect(0, 0, canvas.width, canvas.height);
    predictionDiv.textContent = '';
    initCanvas();
    fileInput.value = ''
});

predictButton.addEventListener("click", function() {
    const image = canvas.toDataURL();

    fetch("/predict", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ image: image })
    })
    .then(response => response.json())
    .then(data => {
        predictionDiv.innerHTML = `LaTeX: <code>${data.latex}</code>`;
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred while predicting the formula');
    });
});

uploadButton.addEventListener("click", function() {
    if (fileInput.files.length === 0) {
        alert('Please select a file to upload.');
        predictionDiv.innerHTML = 'LaTeX: Please provide a handwritten formula or upload an image of the formula.';
        return;
    }

    const file = fileInput.files[0];
    const reader = new FileReader();
    reader.onloadend = function() {
        const base64Image = reader.result.split(',')[1];
        fetch("/predict", {
            method: "POST",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ image: reader.result })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.json();
        })
        .then(data => {
            if(data.latex) {
                predictionDiv.innerHTML = `LaTeX: <code>${data.latex}</code>`;
            } else {
                predictionDiv.textContent = 'Could not convert the formula.';
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred while predicting the formula');
        });
    };
    reader.onerror = function(error) {
        console.error('Error:', error);
        alert('Error reading file');
    };
    reader.readAsDataURL(file);
});

document.querySelector('form').addEventListener('submit', function(event) {
    event.preventDefault();
});