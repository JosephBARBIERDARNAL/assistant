from src.ai import AI
from src.audio import record_audio, save_as_mp3

ai = AI()
recording = record_audio(5)
save_as_mp3(recording, 44100, "audiofiles/input.mp3")
transcript = ai.listen("audiofiles/input.mp3")
response = ai.think(transcript)
ai.speak(response)
print(response)