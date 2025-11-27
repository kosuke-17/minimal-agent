# minimal-agent

Amazon Bedrock AgentCore Runtime を使用した AI エージェントのデプロイ手順です。

## 前提条件

- Python 3.12+
- AWS の認証情報の設定
- Claude Sonnet 4 の基盤モデルアクセスを有効化

## セットアップ

### 1. プロジェクトの初期化と依存パッケージの追加

```bash
uv init
uv add strands-agents bedrock-agentcore bedrock-agentcore-starter-toolkit
```

### 2. エージェントのコード作成

`my_agent.py` を作成します：

```python
from bedrock_agentcore.runtime import BedrockAgentCoreApp
from strands import Agent

app = BedrockAgentCoreApp()
agent = Agent()

@app.entrypoint
def invoke(payload):
    user_message = payload.get("prompt")
    result = agent(user_message)
    return {"result": result.message}

if __name__ == "__main__":
    app.run()
```

## デプロイ

### 1. 設定

```bash
uv run agentcore configure -e my_agent.py
```

### 2. デプロイ実行

```bash
uv run agentcore launch
```

## エージェントの呼び出し

```bash
uv run agentcore invoke '{"prompt": "何か面白いこと言って。"}'
```

## 料金目安

| ユースケース | 月間リクエスト | 処理時間 | 月額 |
|------------|--------------|---------|------|
| シンプルな社内用エージェント | 1万 | 平均15秒 | 約450円 |
| カスタマーサポートエージェント | 10万 | 平均60秒 | 約11,000円 |

※ I/O待ちの時間にはCPUリソースに課金されません

## 参考

- [5分で AI エージェントをデプロイ・ホスティングする – Amazon Bedrock AgentCore Runtime](https://aws.amazon.com/jp/blogs/startup/5min-ai-agent-hosting/)
