from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat_endpoint(req: ChatRequest):
    try:
        response = requests.post(
            "http://localhost:11434/api/chat",
            json={
                "model": "llama3.2-vision:latest",
                "messages": [{"role": "user", "content": req.message}],
                "stream": False
            }
        )
        response.raise_for_status()
        result = response.json()
        
        return {"response": result["message"]["content"]}
    except Exception as e:
        return {"error": str(e)}
