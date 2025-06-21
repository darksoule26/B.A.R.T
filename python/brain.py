import requests
from smart_function import handle_smart_commands

API_URL = "https://openrouter.ai/api/v1/chat/completions"
API_KEY = "YOUR API KEY HERE"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def think(prompt):
    # First check for smart PC-specific commands
    smart_response = handle_smart_commands(prompt)
    if smart_response:
        return smart_response

    # If nothing found, fallback to GPT model
    data = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {"role": "system", "content": "Your name is Bart. You are a smart, witty AI assistant who can help with any PC task. Respond politely, briefly, and informatively."},
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(API_URL, headers=HEADERS, json=data)
        response.raise_for_status()
        result = response.json()
        message = result['choices'][0]['message']['content'].strip()
        return message
    except Exception as e:
        print(f"Error in Brain.py: {e}")
        return "I'm sorry, I couldn't process that request right now."
