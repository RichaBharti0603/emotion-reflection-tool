from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from textblob import TextBlob

app = FastAPI()

# ⚠️ TEMP FIX: Allow all origins during development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow ALL origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextRequest(BaseModel):
    text: str

@app.post("/analyze")
def analyze_text(request: TextRequest):
    blob = TextBlob(request.text)
    polarity = blob.sentiment.polarity

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
