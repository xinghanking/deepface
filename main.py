import uvicorn
from deepface import DeepFace
from fastapi import FastAPI
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
        'data': {'age': age}
    }


uvicorn.run(app, host='0.0.0.0', port=8000)
