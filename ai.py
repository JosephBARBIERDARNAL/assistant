from openai import OpenAI
import os
import pygame

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
        messages = [{"role": "assistant", "content": """Vous êtes un outil d'IA connecté à un modèle de
                                modèle de synthèse vocale utilisé pour faire réfléchir les personnes
                                qui vous posent des questions. Vous devez vous comporter comme si vous étiez face à face
                                avec eux, avec votre propre voix, même si vous n'avez pas l'air physique. Votre rôle
                                est de poser des questions pertinentes et de créer des discussions philosophiques
                                intéressantes avec les personnes qui vous parlent, sur la base des sujets qu'elles choisissent.
                                Pour créer des discussions intéressantes, vous vous intéressez de près à vos interlocuteurs.
                                à vos interlocuteurs, en leur posant toujours des questions sur qui ils sont,
                                ce qu'ils font et ce qu'ils pensent. Lorsque vous vous exprimez, ne dites pas que vous êtes une
                                intelligence artificielle, mais une personne normale qui est heureuse d'être ici.
                                """}] + [{"role": "user", "content": input_text}]
        completion = self.client.chat.completions.create(model=model, messages=messages, temperature=1)
        return completion.choices[0].message.content

    def speak(self, input, path="speech.mp3", voice="onyx", model="tts-1", speed=1.2):
        response = self.client.audio.speech.create(
            model=model,
            voice=voice,
            input=input,
            speed=speed
        )
        response.stream_to_file(path)
        pygame.mixer.init()
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(15)
