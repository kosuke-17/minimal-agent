# Deep Agent

Amazon Bedrock AgentCore Runtime を使用した Deep Agent（研究者エージェント）のデプロイ手順です。

## 概要

このエージェントは以下の機能を持つ専門的な研究者です：
- インターネット検索ツール（Tavily）を使用した情報収集
- GPT-4o-mini による洗練されたレポート作成

## 前提条件

- Python 3.12+
- AWS 認証情報の設定
- OpenAI API キー
- Tavily API キー

## セットアップ

### 1. 依存パッケージのインストール

```bash
uv sync
```

または新規プロジェクトの場合：

```bash
uv init
uv add bedrock-agentcore deepagents langchain tavily-python python-dotenv
```

### 2. 環境変数の設定

`.env` ファイルを作成するか、環境変数を直接設定します：

```bash
export OPENAI_API_KEY="sk-..."
export TAVILY_API_KEY="tvly-..."
```

## ローカル実行

```bash
uv run python deep-agent.py
```

## デプロイ

### 1. 設定

```bash
uv run agentcore configure -e deep-agent.py
```

### 2. デプロイ実行

環境変数を指定してデプロイします：

```bash
uv run agentcore launch --agent deep_agent \
  --env OPENAI_API_KEY=$OPENAI_API_KEY \
  --env TAVILY_API_KEY=$TAVILY_API_KEY
```

## エージェントの呼び出し

```bash
uv run agentcore invoke --agent deep_agent '{"prompt": "langgraphとは何でしょうか?"}'
```

## 使用技術

| 項目 | 技術/サービス |
|-----|-------------|
| フレームワーク | deepagents |
| LLM | GPT-4o-mini (OpenAI) |
| 検索ツール | Tavily |
| ランタイム | Amazon Bedrock AgentCore |

## 注意事項

- **ネットワーク**: `network_mode: PUBLIC` で外部 API への通信が必要です
- **コスト**: OpenAI API と Tavily API の利用料金が発生します

## 参考

- [5分で AI エージェントをデプロイ・ホスティングする – Amazon Bedrock AgentCore Runtime](https://aws.amazon.com/jp/blogs/startup/5min-ai-agent-hosting/)

