# Emotion Reflection Tool

An AI-powered web app that analyzes user text input and reflects the underlying emotion using sentiment analysis.

## 🌐 Live Links

- **Frontend** (Vercel): [emotion-reflection-tool.vercel.app](https://emotion-reflection-tool.vercel.app)
- **Backend** (Render): [emotion-reflection-tool.onrender.com](https://emotion-reflection-tool.onrender.com)

---

## 📌 Features

- 🧠 Emotion detection using TextBlob NLP
- 🎨 Clean, calm UI with background visuals
- 💡 Shows confidence score for emotions
- ⚡ Built with FastAPI + Next.js
- 🌍 Deployed on Render and Vercel

---

## 🛠️ Tech Stack

| Layer     | Tech                  |
|-----------|-----------------------|
| Frontend  | Next.js, TypeScript, CSS Modules |
| Backend   | FastAPI, Python, TextBlob |
| Hosting   | Vercel (frontend), Render (backend) |
| Tools     | GitHub, VSCode, Postman |

---

## 🔁 API Reference

### `POST /analyze`

- **Request Body:**

```json
{
  "text": "I feel amazing today!"
}

🚀 How to Run Locally
Clone the repo:


git clone https://github.com/RichaBharti0603/emotion-reflection-tool.git
cd emotion-reflection-tool
Start backend (in /backend folder):


pip install -r requirements.txt
uvicorn main:app --reload
Start frontend (in /frontend folder):


npm install
npm run dev
Open http://localhost:3000 to use the app locally.

👩‍💻 Built By
Richa Bharti
