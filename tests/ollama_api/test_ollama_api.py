import requests
import pytest

OLLAMA_API_URL = "http://localhost:11434/api/generate"

def test_ollama_generate():
    payload = {
        "model": "llama2",
        "prompt": "Hello, Ollama!",
        "stream": False
    }
    response = requests.post(OLLAMA_API_URL, json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "response" in data
    print("Ollama response:", data["response"])
