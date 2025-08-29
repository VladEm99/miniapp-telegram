import os
from openai import AsyncOpenAI

client = AsyncOpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=os.environ["OPENROUTER_API_KEY"].strip(),
)

async def ai_generate(text: str):
    completion = await client.chat.completions.create(
      model="deepseek/deepseek-chat",
      messages=[
        {
          "role": "user",
          "content": text
        }
      ]
    )
    print(completion)
    return completion.choices[0].message.content