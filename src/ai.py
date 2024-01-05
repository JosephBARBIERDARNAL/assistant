from openai import OpenAI
import os

class AI:
    def __init__(self, api_key=os.environ.get("OPENAI_API_KEY")):
        self.client = OpenAI(api_key=api_key)

    def listen(self, audio_file, model="whisper-1"):
        with open(audio_file, "rb") as file:
            transcript = self.client.audio.transcriptions.create(
                model=model, 
                file=file
            )
        return transcript.text

    def think(self, input_text, model="gpt-3.5-turbo"):
        completion = self.client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": input_text},
            ]
        )
        return completion.choices[0].message.content

    def speak(self, input_text, path="audiofiles/speech.mp3", voice="alloy", model="tts-1"):
        response = self.client.audio.speech.create(
            model=model,
            voice=voice,
            input=input_text
        )
        response.stream_to_file(path)
        os.system(f"afplay {path}")
