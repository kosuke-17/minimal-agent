# 実装履歴: LangGraph + OpenAI エージェント

**日時**: 2025-11-27

## 実装内容

既存の strands-agents エージェント（`my_agent.py`）と並行して、LangGraph + OpenAI を使用した新しいエージェントを Bedrock AgentCore にデプロイする実装を追加しました。

## 作成・更新したファイル

### 1. `langgraph_agent.py` (新規作成)

LangGraph を使用したシンプルなチャットボットエージェント:

- `StateGraph` による状態管理
- `ChatOpenAI` (gpt-4o) による応答生成
- `BedrockAgentCoreApp` との統合

### 2. `pyproject.toml` (更新)

以下の依存関係を追加:

- `langgraph>=0.2.0`
- `langchain-openai>=0.2.0`

### 3. `README.md` (更新)

- 両エージェントの一覧表
- LangGraph エージェントのセットアップ・デプロイ手順
- 環境変数設定の説明

## デプロイ手順

```bash
# 1. 環境変数設定
export OPENAI_API_KEY="sk-..."

# 2. 依存関係インストール
uv sync

# 3. エージェント設定
uv run agentcore configure -e langgraph_agent.py

# 4. デプロイ
uv run agentcore launch --agent langgraph_agent

# 5. テスト
uv run agentcore invoke --agent langgraph_agent '{"prompt": "Hello!"}'
```

## ファイル構成

```
minimal-agent/
├── my_agent.py              # strands-agents (Bedrock Claude)
├── langgraph_agent.py       # LangGraph + OpenAI (新規)
├── pyproject.toml           # 依存関係 (更新)
├── README.md                # ドキュメント (更新)
├── README.bedrock.md        # Bedrock エージェント詳細
└── docs/
    └── implementation-log-langgraph-openai.md  # この履歴
```

