import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)
client = OpenAI(base_url="https://openrouter.ai/api/v1",
                api_key=os.getenv("OPENROUTER_API_KEY"))

models = ["google/gemma-4-26b-a4b-it", "meta-llama/llama-3.1-8b-instruct"]
prompt = "Can you create a pancake recipe for four people with healthy substitutes explained?"

with open("outputs.txt", "w", encoding="utf-8") as f:
    for m in models:
        r = client.chat.completions.create(model=m, messages=[{"role": "user", "content": prompt}], max_tokens=800)
        text = f"=== {m} ===\n{r.choices[0].message.content}\n"
        print(text)
        f.write(text + "\n")