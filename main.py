import os
from fastapi import FastAPI
from schemas import ChatRequest, ChatResponse
from openai import generate_response

app = FastAPI()

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')


@app.post("/complete_chat", response_model=ChatResponse)
async def complete_chat(chat_request: ChatRequest):
    try:
        user_input = chat_request.partial_text
        response = generate_response(user_input)
        if response:
            return {"completed_text": response}
    except Exception as e:
        raise e


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
