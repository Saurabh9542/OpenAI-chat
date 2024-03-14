import requests
import os


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
    try:
        response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=data)
        if response.status_code == 200:
            return response.json()['choices'][0]['message']['content']
        else:
            return response.json()['error']['message']
    except requests.exceptions.HTTPError as e:
        error_message = response.json().get('error', str(e))
        return f"OpenAI API Error: {error_message}"
    except Exception as e:
        return f"Error: {str(e)}"

