from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import requests

from jobs import get_job

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    sender: str
    text: str

class ChatRequest(BaseModel):
    session_id: str
    message: str

@app.post("/chat")
async def chat_endpoint(req: ChatRequest):
    try:
        job = get_job(req.session_id)

        # Add user's message
        job.add_message("user", req.message)

        response = requests.post(
            "http://localhost:11434/api/chat",
            json={
                "model": "llama3.2:latest",
                "messages": job.get_history(),
                "stream": False
            }
        )
        response.raise_for_status()
        result = response.json()

        # Add bot response to history
        job.add_message("assistant", result["message"]["content"])

        return {"response": result["message"]["content"]}

    except Exception as e:
        return {"error": str(e)}