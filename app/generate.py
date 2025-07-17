from openai import OpenAI
from config import API_KEY, API_KEY2

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=API_KEY2,
)

completion = client.chat.completions.create(
  # extra_headers={
  #   "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
  #   "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
  # },
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
print(completion.choices[0].message.content)