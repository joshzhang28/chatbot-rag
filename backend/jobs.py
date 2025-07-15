from collections import defaultdict
from typing import List
import uuid

class Job:
    def __init__(self, session_id: str):
        self.session_id = session_id
        self.messages: List[dict] = []

    def add_message(self, role: str, content: str):
        self.messages.append({"role": role, "content": content})

    def get_history(self) -> List[dict]:
        return self.messages

    def clear(self):
        self.messages.clear()

# Global in memory store for jobs
job_store = defaultdict(lambda: Job(session_id=str(uuid.uuid4())))

def get_job(session_id: str) -> Job:
    return job_store[session_id]
