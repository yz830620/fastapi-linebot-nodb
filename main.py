from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()


class Intensity(Enum):
    STRONG = "Strong"
    MEDIUM = "Medium"
    LITTLE = "Little"


class ExerciseLog(BaseModel):
    name: str
    duration: int
    intensity: Intensity
    date: str


items = {
    0: ExerciseLog(
        name="HIIT", duration=8, intensity=Intensity.MEDIUM, date=str(datetime.now())
    ),
    1: ExerciseLog(
        name="GYM", duration=55, intensity=Intensity.STRONG, date=str(datetime.now())
    ),
    2: ExerciseLog(
        name="Biking", duration=30, intensity=Intensity.LITTLE, date=str(datetime.now())
    ),
}


@app.get("/")
def index() -> dict[str, dict[int, ExerciseLog]]:
    return {"items": items}
