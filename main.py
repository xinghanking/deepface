import numpy
import uvicorn
from deepface import DeepFace
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(client_max_size=1024 * 1024 * 10)


class Item(BaseModel):
    avatar_path: str
    avatar_data: str = None


@app.post('/analyze')
async def analyze(item: Item):
    if item.avatar_data is not None and item.avatar_data.strip() != '':
        image = numpy.frombuffer(item.avatar_data)
    else:
        if item.avatar_path is not None and item.avatar_path.strip() != '':
            image = item.avatar_path
        else:
            return {
                "code": 1
            }

    info = DeepFace.analyze(image, ('age', 'gender'))
    age = info[0]["age"]
    return {
        "code": 0,
        "data": {"age": age}
    }
