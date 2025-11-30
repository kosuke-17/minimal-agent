import os
from typing import Literal

from bedrock_agentcore.runtime import BedrockAgentCoreApp
from deepagents import create_deep_agent
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from tavily import TavilyClient

load_dotenv()

tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


# create a search tool
def internet_search(
    query: str,
    max_results: int = 5,
    topic: Literal["general", "news", "finance"] = "general",
    include_raw_content: bool = False,
):
    """Run a web search"""
    return tavily_client.search(
        query,
        max_results=max_results,
        include_raw_content=include_raw_content,
        topic=topic,
    )


# create a deep agent
research_instruction = """
あなたは専門的な研究者です。あなたの仕事は、徹底的な調査を行い、洗練されたレポートを作成することです。

あなたは、情報収集の主要な手段としてインターネット検索ツールを利用できます。

internet_search
これは、与えられたクエリでインターネット検索を実行するために使用します。
返される結果の最大数、トピック、および生のコンテンツを含めるかどうかを指定できます。
"""

model = init_chat_model(
    model="gpt-4o-mini",
)


agent = create_deep_agent(
    tools=[internet_search],
    system_prompt=research_instruction,
    model=model,
)

# result = agent.invoke(
#     {"messages": [{"role": "user", "content": "langgraphとは何でしょうか?"}]}
# )

# # Print the agent's response
# print(result["messages"][-1].content)

app = BedrockAgentCoreApp()


@app.entrypoint
def invoke(payload):
    user_message = payload.get("prompt")
    result = agent.invoke({"messages": [{"role": "user", "content": user_message}]})
    return {"result": result["messages"][-1].content}


if __name__ == "__main__":
    app.run()
