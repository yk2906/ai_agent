from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI()

### 以下から実装内容
# response = client.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {"role": "user", "content": "こんにちは！私はジョンと言います！"},
#     ],
#     stream=True,
# )

# for chunk in response:
#     content = chunk.choices[0].delta.content
#     if content is not None:
#         print(content, end="", flush=True)

# client = OpenAI()

# response = client.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[
#         {
#             "role": "system",
#             "content": '人物一覧を次のJSON形式で出力してください。\n{"people": ["aaa", "bbb"]}',
#         },
#         {
#             "role": "user",
#             "content": "昔々あるところにおじいさんとおばあさんがいました",
#         },
#     ],
#     response_format={"type": "json_object"},
# )
# print(response.choices[0].message.content)

image_url = "https://www.fcbarcelona.com/photo-resources/2021/08/09/276ad270-e5c6-453d-8d9f-212417ad7cb3/Camp-Nou-3.jpg?width=1200&height=750"

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "画像を説明してください。"},
                {"type": "image_url", "image_url": {"url": image_url}},
            ],
        }
    ],
)

print(response.choices[0].message.content)