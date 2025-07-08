from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random

app = FastAPI()

# ✅ Add CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://emotion-reflection-tool.vercel.app"],  # 👈 frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextInput(BaseModel):
    text: str

@app.post("/analyze")
def analyze_text(input: TextInput):
    # Fake response logic
    emotions = ["Happy", "Sad", "Angry", "Excited", "Anxious"]
    response = {
        "emotion": random.choice(emotions),
        "confidence": round(random.uniform(0.7, 0.99), 2)
    }
    return response
