import requests
import os
import sys

# 推荐从环境变量中读取 API Key，更安全
OPENROUTER_API_KEY = "sk-vobhnalamqxulbhbfwzndyrxfhvijcfgdsjinmxhwwdctpaq"

OPENROUTER_API_URL = "https://api.siliconflow.cn/v1/chat/completions"

def chat_with_openrouter(prompt, model="Qwen/Qwen3-8B"):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": model,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(OPENROUTER_API_URL, headers=headers, json=payload)
        response.raise_for_status()  # 抛出非 200 错误
        data = response.json()

        if "choices" in data:
            message = data["choices"][0]["message"]["content"]
            print(f"🤖 模型回复:\n{message}")
        else:
            print("❌ 响应中没有 'choices' 字段。完整响应：", data)

    except requests.exceptions.RequestException as e:
        print("❌ 请求出错:", e)
        if response is not None:
            print("响应内容:", response.text)

if __name__ == "__main__":
    user_input = input("请输入你的问题: ")
    chat_with_openrouter(user_input)
