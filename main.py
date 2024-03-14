import requests
import os
from fastapi import FastAPI, HTTPException, Header
from schemas import ChatRequest, ChatResponse

app = FastAPI()

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')


def generate_response(user_input: str) -> str:
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + OPENAI_API_KEY
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": user_input}],
        "temperature": 0.7
    }
    response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=data)
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return None


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
