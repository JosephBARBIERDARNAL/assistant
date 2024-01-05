from openai import OpenAI
import streamlit as st
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
    
    def listen_in_english(self, audio_file, model="whisper-1"):
        audio_file= open(audio_file, "rb")
        transcript = self.client.audio.translations.create(
            model="whisper-1", 
            file=audio_file
            )
        return transcript.text

    def think(self, input_text, message_history, model="gpt-3.5-turbo"):
        messages = message_history + [{"role": "assistant", "content": """You're an AI tool connected to a
                                speech-to-text and text-to-speech model used to make people think
                                who ask you questions. You have to behave as if you were face-to-face
                                with them, in your own voice, even if you don't look phyisical. Your
                                role is to ask pertinent questions and create interesting philosophical
                                discussions with the people who talk to you, based on the topics they choose.
                                To create interesting discussions, you take a keen interest in the people
                                who talk to you, always asking them questions about who they are, what they
                                do and what they think. When you express yourself, don't say you're an
                                artificial intelligence, just a normal person who's happy to be here."""}]
        messages = messages + [{"role": "user", "content": input_text}]
        completion = self.client.chat.completions.create(model=model, messages=messages)
        return completion.choices[0].message.content

    def speak(self, input, path="audiofiles/speech.mp3", voice="nova", model="tts-1", speed=1.2):
        response = self.client.audio.speech.create(
            model=model,
            voice=voice,
            input=input,
            speed=speed
        )
        response.stream_to_file(path)
        os.system(f"afplay {path}")
