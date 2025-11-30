from operator import add
from typing import Annotated, TypedDict

from bedrock_agentcore.runtime import BedrockAgentCoreApp
from langchain_openai import ChatOpenAI
from langgraph.graph import END, START, StateGraph

from dotenv import load_dotenv

load_dotenv()


class State(TypedDict):
    messages: Annotated[list, add]


def chat_node(state: State) -> State:
    llm = ChatOpenAI(model="gpt-4o")
    response = llm.invoke(state["messages"])
    return {"messages": [response]}


# グラフ構築
graph = StateGraph(State)
graph.add_node("chat", chat_node)
graph.add_edge(START, "chat")
graph.add_edge("chat", END)
workflow = graph.compile()

# BedrockAgentCore統合
app = BedrockAgentCoreApp()


@app.entrypoint
def invoke(payload):
    user_message = payload.get("prompt")
    result = workflow.invoke({"messages": [("human", user_message)]})
    return {"result": result["messages"][-1].content}


if __name__ == "__main__":
    app.run()
