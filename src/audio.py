import sounddevice as sd
from pydub import AudioSegment
import numpy as np
import io

def record_audio(duration, sample_rate=44100, channels=1, device=None):
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=channels, device=device)
    sd.wait()  # Wait until recording is finished
    return recording

def save_as_mp3(audio_data, sample_rate, filename, channels=1):
    audio_segment = AudioSegment(
        data=np.array(audio_data).tobytes(),
        sample_width=audio_data.dtype.itemsize,
        frame_rate=sample_rate,
        channels=channels
    )
    audio_segment.export(filename, format="mp3")