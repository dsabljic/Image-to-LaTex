const canvas = document.getElementById("inputCanvas");
const ctx = canvas.getContext("2d");
const predictButton = document.getElementById("predictBtn");
const clearButton = document.getElementById("clearBtn");
const predictionDiv = document.getElementById("prediction");

function initCanvas() {
    ctx.fillStyle = "white";
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.lineWidth = 7;
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
    initCanvas();
});

predictButton.addEventListener("click", function() {
    canvas.toBlob(blob => {
        const formData = new FormData();
        formData.append("image", blob);

        fetch("/predict_formula", {
            method: "POST",
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            predictionDiv.textContent = `Predicted LaTeX: ${data.latex}`;
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred while predicting the formula');
        });
    });
});