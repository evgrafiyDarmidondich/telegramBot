from openai import AsyncOpenAI
from config import API_KEY, API_KEY2

client = AsyncOpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=API_KEY2,
)


async def generate(text: str):
    completion = await client.chat.completions.create(
        extra_body={},
        model="deepseek/deepseek-chat-v3-0324:free",
        messages=[
            {
                "role": "user",
                "content": "Привет",
                "temterature": "0.0"
            }
        ]
      )
    print(completion)
    return completion.choices[0].message.content