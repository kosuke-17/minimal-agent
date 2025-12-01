from langchain_ollama import ChatOllama

# https://reference.langchain.com/python/integrations/langchain_ollama/?_gl=1*1wnvxxa*_gcl_au*OTg4NjcwMTExLjE3NjQwNTEzNTA.*_ga*MTE1Mzg3NTQ2LjE3NjQwNTEzNTA.*_ga_47WX3HKKY2*czE3NjQ1NjgzMzMkbzYkZzAkdDE3NjQ1NjgzMzMkajYwJGwwJGgw#langchain_ollama.ChatOllama
model = ChatOllama(
    model="gpt-oss:20b",
    validate_model_on_init=True,
    temperature=0.8,
    num_predict=256,
)

messages = [
    (
        "system",
        "あなたは英語から日本語に変換するアシスタントです。与えられた文章を日本語に変換してください。",
    ),
    ("user", "Get started using Ollama chat models in LangChain."),
]

for chunk in model.stream(messages):
    print(chunk.content, end="", flush=True)
