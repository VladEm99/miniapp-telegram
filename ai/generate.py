import os
from openai import AsyncOpenAI

client = AsyncOpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=os.environ["OPENROUTER_API_KEY"].strip(),
)

async def ai_generate(text: str):
    completion = await client.chat.completions.create(
      model="anthropic/claude-sonnet-4.5",
      messages=[
        {
          "role": "user",
          "content": text
        }
      ]
    )
    print(completion)
    return completion.choices[0].message.content