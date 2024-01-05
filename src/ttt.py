from openai import OpenAI
import os

def text_to_text(input, client=OpenAI(api_key=os.environ.get("OPENAI_API_KEY")),
                 model="gpt-3.5-turbo"):

    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": input},
            ]
        )
    return completion.choices[0].message.content

output = text_to_text("Hello, my name is John. I am a robot.")
print(output)