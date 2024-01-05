from openai import OpenAI
import os


def speech_to_text(audio_file, client=OpenAI(api_key=os.environ.get("OPENAI_API_KEY")),
                   model="whisper-1"):

    audio_file= open(audio_file, "rb")
    transcript = client.audio.transcriptions.create(
        model=model, 
        file=audio_file
        )
    return transcript.text

output = speech_to_text("audiofiles/speech.mp3")
print(output)