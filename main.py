from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from converter import get_latex_from_image
from pydantic import BaseModel

app = FastAPI()

class ImageData(BaseModel):
    image: str

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def read_index():
    return FileResponse('templates/index.html')

@app.post("/predict")
async def predict_formula(data: ImageData):
    try:
        base64_image = data.image.split(",")[1]
        latex_code = get_latex_from_image(base64_image)
        return {"latex": latex_code}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/upload_predict")
async def predict_formula(data: ImageData):
    pass
