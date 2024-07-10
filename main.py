from fastapi import FastAPI
from deepface import DeepFace
from pydantic import BaseModel

app = FastAPI()
class Item(BaseModel):
    avatar_path: str

@app.post('/analyze')
async def analyze(item: Item):
    avatar_path = item.avatar_path
    info = DeepFace.analyze(avatar_path, ('age'))
    age = info[0]["age"]
    return {
        'code': 0,
        'age': age
    }