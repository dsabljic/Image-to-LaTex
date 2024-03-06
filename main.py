from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def read_index():
    return FileResponse('template/index.html')

@app.post("/predict")
async def predict_formula(image: UploadFile = File(...)):
    # Dummy function to 'process' the image
    # In a real scenario, you would add image processing logic here

    # Return a generic LaTeX formula for demonstration purposes
    generic_latex = "E=mc^2"
    return JSONResponse(content={"latex": generic_latex})