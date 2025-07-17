import requests

OLLAMA_API_URL = "http://localhost:11434/api/generate"

def test_ollama_generate(model, prompt):
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }

    try:
        print(f"🔍 Testing model: {model}")
        print(f"💬 Prompt: {prompt}")
        
        response = requests.post(OLLAMA_API_URL, json=payload)
        
        if response.status_code == 200:
            data = response.json()
            if "response" in data:
                print(f"✅ Success! Response:")
                print(data["response"])
            else:
                print(f"❌ Error: Response JSON missing 'response' key")
                print(f"Received: {response.text}")
        else:
            print(f"❌ Error: Unexpected status code {response.status_code}")
            print(f"Response: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("❌ Failed to connect to Ollama server. Is it running on localhost:11434?")

# 直接调用测试函数
if __name__ == "__main__":
    test_ollama_generate("qwen3:1.7b", "你好，请简单介绍一下你自己。")