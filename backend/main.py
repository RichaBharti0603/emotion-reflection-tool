from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Reflection(BaseModel):
    text: str

@app.post("/analyze")
def analyze(reflection: Reflection):
    emotions = [
        {"emotion": "Happy", "confidence": 0.92},
        {"emotion": "Anxious", "confidence": 0.85},
        {"emotion": "Excited", "confidence": 0.88},
        {"emotion": "Sad", "confidence": 0.75},
        {"emotion": "Confused", "confidence": 0.80},
        {"emotion": "Hopeful", "confidence": 0.90},
    ]
    return random.choice(emotions)
