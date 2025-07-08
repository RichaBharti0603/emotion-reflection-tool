from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from textblob import TextBlob

app = FastAPI()

# Allow only the correct frontend origins
origins = [
    "http://localhost:3000",
    "https://emotion-reflection-tool.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextRequest(BaseModel):
    text: str

@app.post("/analyze")
def analyze_text(request: TextRequest):
    blob = TextBlob(request.text)
    polarity = blob.sentiment.polarity  # range -1.0 to 1.0

    if polarity > 0.3:
        emotion = "Happy"
    elif polarity < -0.3:
        emotion = "Sad"
    else:
        emotion = "Neutral"

    confidence = round(abs(polarity), 2)

    return {
        "emotion": emotion,
        "confidence": confidence
    }
