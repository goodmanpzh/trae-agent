from enum import Enum

class LLMProvider(Enum):
    OLLAMA = "ollama"
    OPENAI = "openai"

# 字符串转枚举成员
provider_str = "ollama"
provider_enum = LLMProvider(provider_str)

print(provider_enum)  # 输出：LLMProvider.OLLAMA
print(provider_enum.value)  # 输出："ollama"（成员对应的字符串值）
print(provider_enum is LLMProvider.OLLAMA)  # 输出：True（确实是目标枚举成员）