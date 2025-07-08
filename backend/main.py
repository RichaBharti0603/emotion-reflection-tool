from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random

app = FastAPI()

# ✅ CORS: Allow both local and deployed frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://emotion-reflection-tool.vercel.app",  # deployed frontend
        "http://localhost:3000"                        # local dev
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Input schema
class TextInput(BaseModel):
    text: str

# ✅ API route
@app.post("/analyze")
def analyze_text(input: TextInput):
    # Fake emotion detection logic
    emotions = ["Happy", "Sad", "Angry", "Excited", "Anxious"]
    response = {
        "emotion": random.choice(emotions),
        "confidence": round(random.uniform(0.7, 0.99), 2)
    }
    return response
