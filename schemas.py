from pydantic import BaseModel

class ChatRequest(BaseModel):
    partial_text: str

class ChatResponse(BaseModel):
    completed_text: str