import os
import time
from argparse import ArgumentParser
import wave

from pyaudio import paInt16, PyAudio, get_sample_size

BASE_DIRECTORY = "./output"
FORMAT = paInt16  # 16-bit resolution
CHANNELS = 1              # 1 channel (mono)
RATE = 44100              # 44.1kHz sampling rate
CHUNK = 1024              # 2^10 samples for buffer
RECORD_SECONDS = 2        # Duration of recording

def get_argument() -> tuple[str, int]:
    parser = ArgumentParser()
    parser.add_argument("word", type=str, help="Word of recording")
    parser.add_argument("duration", type=str, help="Duration of recording")
    args = parser.parse_args()
    return args.word.strip(), int(args.duration.strip())

def create_directory(base_dir: str, sub_dir: str) -> str:
    output_dir = os.path.join(f"{base_dir}", sub_dir)
    os.makedirs(output_dir, exist_ok=True)
    return output_dir

def get_audio_output_path(path_dir: str) -> str:
    time_record = time.time()
    return os.path.join(path_dir, f"{time_record}.wav")

def start_record(duration: int) -> list[bytes]:
    audio = PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
    frames = []
    print("Recording...")
    for _ in range(0, int(RATE / CHUNK * duration)):
        data = stream.read(CHUNK)
        frames.append(data)
    stream.stop_stream()
    stream.close()
    audio.terminate()
    print("Finished recording.")
    return frames
    
def save_audio(frames: list[bytes], output_path: str): 
    try:
        with wave.open(output_path, 'wb') as wf:
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b''.join(frames))
        print(f"Audio saved as {output_path}")
    except Exception as e:
        print(f"An error occurred while saving the audio file: {e}")

def main():
    print("# ----------------------------------------------- #")
    print("# Word sound software to create data for training #")
    print("# ------- Author: Sivaroot Chuncharoen ---------- #")
    print("# --------------- Version: 1.0.0 ---------------- #")
    print("# ----------------------------------------------- #\n\n")
    
    word, duration = get_argument()
    dir_path = create_directory(BASE_DIRECTORY, word)
    output_path = get_audio_output_path(dir_path)
    audio_frames = start_record(duration)
    save_audio(audio_frames, output_path)
    
if __name__ == "__main__":
    main()