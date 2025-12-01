"""
Ollamaを使用したエージェント

https://docs.langchain.com/oss/python/integrations/chat/ollama
"""

from langchain_ollama import ChatOllama

# 難易度: 簡単
llm = ChatOllama(
    model="llama3.2:3b",
    temperature=0,
)

messages = [
    (
        "system",
        "あなたは英語から日本語に変換するアシスタントです。与えられた文章を日本語に変換してください。",
    ),
    ("user", "Get started using Ollama chat models in LangChain."),
]


ai_message = llm.invoke(messages)
print(ai_message)
