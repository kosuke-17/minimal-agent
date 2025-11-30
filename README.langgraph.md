# minimal-agent

Amazon Bedrock AgentCore Runtime を使用した AI エージェントプロジェクトです。

## エージェント一覧

| エージェント | ファイル | フレームワーク | モデル |
|-------------|---------|--------------|-------|
| my_agent | `my_agent.py` | strands-agents | Claude (Bedrock) |
| langgraph_agent | `langgraph_agent.py` | LangGraph | GPT-4o (OpenAI) |

## セットアップ

### 前提条件

- Python 3.12+
- AWS 認証情報の設定
- OpenAI API キー（LangGraph エージェント用）

### 依存関係のインストール

```bash
uv sync
```

## LangGraph + OpenAI エージェント

### 環境変数の設定

```bash
export OPENAI_API_KEY="sk-..."
```

### エージェントの設定

```bash
uv run agentcore configure -e langgraph_agent.py
```

### デプロイ

- `--env OPEN_API_KEY=XXXX`とやることで環境変数の設定ができる
- `uv run agentcore launch --help`で必要なコマンドがわかる

```bash
uv run agentcore launch --agent langgraph_agent
```

### 呼び出し

```bash
uv run agentcore invoke --agent langgraph_agent '{"prompt": "Hello!"}'
```

## Strands エージェント（Bedrock Claude）

詳細は [README.bedrock.md](README.bedrock.md) を参照してください。

### デプロイ

```bash
uv run agentcore launch --agent my_agent
```

### 呼び出し

```bash
uv run agentcore invoke --agent my_agent '{"prompt": "何か面白いこと言って。"}'
```

## 注意事項

- **ネットワーク**: 両エージェントとも `network_mode: PUBLIC` で外部 API への通信が可能です
- **コスト**: OpenAI API / Bedrock の利用料金が発生します

