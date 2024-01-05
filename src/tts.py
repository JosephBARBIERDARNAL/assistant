from openai import OpenAI
import os 

def text_to_speech(input, client=OpenAI(api_key=os.environ.get("OPENAI_API_KEY")),
                   path="audiofiles/speech.mp3", voice="alloy", model="tts-1"):
    
    # Create the audio file on the local machine
    response = client.audio.speech.create(
        model=model,
        voice=voice,
        input=input
        )
    response.stream_to_file(path)

    # Play the audio file
    os.system(f"afplay {path}")

text_to_speech('Hello, my name is John. I am a robot.')