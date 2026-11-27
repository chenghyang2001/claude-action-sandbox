# claude-action-sandbox

這個 repo 是用來測試 **Claude Code GitHub Action**（`anthropics/claude-code-action@v1`）的沙盒。

- 認證方式：Max 訂閱的 OAuth token（secret `CLAUDE_CODE_OAUTH_TOKEN`），**不使用** `ANTHROPIC_API_KEY`。
- `calc.py` 的 `average()` 故意留了一個 bug：空 list 會除以零。
- 在 issue 或留言裡寫 `@claude ...`，Action 會讓 Claude 修程式、推新分支，並在留言附上開 PR 的連結。

## 執行測試

```bash
python -m unittest -v
```
