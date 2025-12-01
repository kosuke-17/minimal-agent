import os
from typing import Optional

from dotenv import load_dotenv
from langchain.messages import AIMessage
from langchain.tools import tool
from langchain_ollama import ChatOllama
from tavily import TavilyClient

load_dotenv()

tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


@tool
def get_weather(city: str, date: Optional[str] = "today") -> dict:
    """Get weather information for a given city and date using Tavily search.

    Args:
        city (str): Name of the city.
        date (str, optional): Defaults to "today".
    """
    print(f"get_weather called with city: {city}, date: {date}")
    query = f"{city} {date} 天気予報 weather forecast"
    result = tavily_client.search(
        query=query,
        max_results=3,
        topic="general",
    )

    print(result)
    return {
        "city": city,
        "date": date,
        "search_results": result.get("results", []),
    }


llm = ChatOllama(
    model="gpt-oss:20b",
    # validate_model_on_init=True,
    temperature=0,
).bind_tools([get_weather])


messages = [
    (
        "system",
        "あなたは天気予報アシスタントです。get_weatherツールを使用して天気予報を取得してください。",
    ),
    ("user", "明日の東京の天気はどうなるでしょうか？"),
]

# ツール名と関数のマッピング
tools_map = {"get_weather": get_weather}

result = llm.invoke(messages)
print("LLM Response:", result)

# ツール呼び出しがあれば実行
if isinstance(result, AIMessage) and result.tool_calls:
    for tool_call in result.tool_calls:
        tool_name = tool_call["name"]
        tool_args = tool_call["args"]
        print(f"\n=== ツール実行: {tool_name}({tool_args}) ===")

        # ツールを実際に呼び出す
        tool_result = tools_map[tool_name].invoke(tool_args)
        print(f"ツール結果: {tool_result}")


# llm = ChatOllama(
#     model="gpt-oss:20b",
#     temperature=0,
# )


# result = llm.invoke(
#     [
#         (
#             "system",
#             "あなたは天気予報アシスタントです。",
#         ),
#         ("user", "明日の東京の天気はどうなるでしょうか？"),
#     ]
# )


# print(result)
