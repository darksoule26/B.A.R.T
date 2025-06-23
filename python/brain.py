import requests

API_URL = "https://openrouter.ai/api/v1/chat/completions"
API_KEY = "your api key"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def think(prompt):
    data = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {"role": "system", "content": "Your name is Bart. You are a smart AI assistant who helps with anything from tech to cooking, jokes, education, or casual conversation. Respond politely, informatively, and with fun energy."},
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
        print(f"Error in brain.py: {e}")
        return "I'm sorry, I couldn't process that request right now."
