from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random

app = FastAPI()

# ✅ CORS settings — must include both deployed and localhost
origins = [
    "https://emotion-reflection-tool.vercel.app",  # Production frontend
    "http://localhost:3000"                        # Local frontend
]

# ✅ Add CORS middleware with all necessary flags
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],      # Allow all HTTP methods
    allow_headers=["*"],      # Allow all headers
)

# ✅ Request schema
class TextInput(BaseModel):
    text: str

# ✅ API endpoint
@app.post("/analyze")
def analyze_text(input: TextInput):
    emotions = ["Happy", "Sad", "Angry", "Excited", "Anxious"]
    response = {
        "emotion": random.choice(emotions),
        "confidence": round(random.uniform(0.7, 0.99), 2)
    }
    return response
