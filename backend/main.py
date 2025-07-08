from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random

app = FastAPI()

# ✅ Explicit origins list
origins = [
    "https://emotion-reflection-tool.vercel.app",
    "http://localhost:3000"
]

# ✅ CORS middleware with full headers
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# ✅ Request body schema
class TextInput(BaseModel):
    text: str

@app.post("/analyze")
def analyze_text(input: TextInput):
    emotions = ["Happy", "Sad", "Angry", "Excited", "Anxious"]
    return {
        "emotion": random.choice(emotions),
        "confidence": round(random.uniform(0.7, 0.99), 2)
    }
