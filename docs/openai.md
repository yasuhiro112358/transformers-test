# OpenAI API for Python
- OpenAI APIを使用する際に必要なもの

```bash
# OpenAIが提供するライブラリ
https://github.com/openai/openai-python
pip install openai
pip install tiktoken
```



## Asynchronous Requests
- use AsyncOpenAI instance instead of OpenAI instance
```python  
from openai import AsyncOpenAI
api_key: str = os.environ.get("OPENAI_API_KEY")
client = AsyncOpenAI(api_key=api_key)
```

## Error Handling
https://github.com/openai/openai-python?tab=readme-ov-file#handling-errors
- All errors inherit from openai.APIError.