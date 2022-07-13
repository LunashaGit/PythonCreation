import os
import openai

from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.environ.get('OPENAI_KEY')
completion = openai.Completion()

def ask(question):
    prompt = f'{question}\n'
    response = completion.create(
        prompt=prompt, engine="ada", stop=[question], temperature=0.5,
        top_p=1, frequency_penalty=0, presence_penalty=0, best_of=1,
        max_tokens=60)
    answer = response.choices[0].text.strip()
    return "Bot : " + answer
