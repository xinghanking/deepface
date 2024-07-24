import logging
from deepface import DeepFace
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class Iterm(BaseModel):
    avatar_path: str = None
    avatar_data: str = None


@router.post("/analyze")
async def analyze(item: Iterm):
    if item.avatar_data is not None and item.avatar_data.strip() != '':
        image = item.avatar_data
    else:
        if item.avatar_path is not None and item.avatar_path.strip() != '':
            image = item.avatar_path
        else:
            return {
                "code": 1
            }

    info = DeepFace.analyze(image, ('age'))
    logging.debug(info)
    age = info[0]["age"]
    return {
        "code": 1,
        "data": {
            "age": age,
            "region": info[0]["region"]
        }
    }
