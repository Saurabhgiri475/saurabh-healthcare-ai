import requests

def medical_chatbot(question):

    prompt = f"""
You are a medical assistant.

Answer this question about diabetes:

{question}
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model":"llama3",
            "prompt":prompt,
            "stream":False
        }
    )

    return response.json()["response"]