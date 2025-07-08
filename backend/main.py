from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from textblob import TextBlob

# Create FastAPI instance
app = FastAPI()

# Allow frontend origins (localhost + vercel)
origins = [
    "http://localhost:3000",
    "https://emotion-reflection-tool.vercel.app"
]

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,              # restrict to frontend URLs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Input schema
class TextRequest(BaseModel):
    text: str

# Emotion analysis route
@app.post("/analyze")
def analyze_text(request: TextRequest):
    blob = TextBlob(request.text)
    polarity = blob.sentiment.polarity  # range: -1.0 (negative) to 1.0 (positive)

    # Simple logic for mock emotion classification
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
