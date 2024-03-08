from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

import converter

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def read_index():
    return FileResponse('templates/index.html')

# demo
@app.post("/predict")
async def predict_formula(image: UploadFile = File(...)):
    # Image processing
    
    generic_latex = converter.get_latex(img_path)
    return JSONResponse(content={"latex": generic_latex})
