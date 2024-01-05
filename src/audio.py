import sounddevice as sd
from pydub import AudioSegment
import numpy as np
import webrtcvad

def record_audio_vad(sample_rate=44100, channels=1, device=None):
    vad = webrtcvad.Vad(1)  # Set aggressiveness level
    vad_frame_length = 30  # ms - WebRTC VAD supports 10, 20 or 30 ms frames
    samples_per_frame = int(sample_rate * vad_frame_length / 1000)
    silent_duration_to_stop = 2000  # ms
    silent_time = 0

    audio_data = np.array([], dtype=np.int16)  # Ensure the correct dtype for VAD

    with sd.InputStream(samplerate=sample_rate, channels=channels, dtype='int16', device=device) as stream:
        while True:
            try:
                frame, overflowed = stream.read(samples_per_frame)
                if overflowed:
                    print("Warning: Buffer overflow occurred. Frame might be corrupted.")

                is_speech = vad.is_speech(frame.tobytes(), sample_rate)

                if is_speech:
                    silent_time = 0
                    audio_data = np.append(audio_data, frame)
                else:
                    silent_time += vad_frame_length
                    if silent_time > silent_duration_to_stop:
                        break

            except Exception as e:
                print(f"Error while processing frame: {e}")
                break

    return audio_data

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