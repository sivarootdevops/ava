import io

from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play


def notify(text: str):
    tts = gTTS(text=text, lang='en', slow=False, lang_check=False, tld='us')
    audio = io.BytesIO()
    tts.write_to_fp(audio)
    audio.seek(0)
    play(AudioSegment.from_file(audio, format="mp3"))
        
def notify_from_mp3(path: str):
    play(AudioSegment.from_mp3(path))