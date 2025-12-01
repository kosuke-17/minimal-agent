import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model

# 環境変数に、langsmithのAPIキーを設定すれば計測される
load_dotenv()


def get_weather(city: str) -> str:
    """Get the weather for a given city"""
    return f"{city}の天気は晴れです。"


tools = [get_weather]
model = init_chat_model(
    model="gpt-4o-mini", temperature=0, api_key=os.getenv("OPENAI_API_KEY")
)

agent = create_agent(
    tools=tools,
    model=model,
    system_prompt="あなたは天気予報アシスタントです。get_weatherツールを使用して天気予報を取得してください。",
)

result = agent.invoke({"input": "明日の東京の天気はどうなるでしょうか？"})
print(result)
