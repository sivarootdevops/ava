import io

from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play


class Notifier:
    def __init__(self, language = 'en', tld='us') -> None:
        self.language = language
        self.tld = tld

        
    def notify(self, text: str):
        tts = gTTS(text=text, lang=self.language, slow=False, lang_check=False, tld=self.tld)
        audio = io.BytesIO()
        tts.write_to_fp(audio)
        audio.seek(0)
        play(AudioSegment.from_file(audio, format="mp3"))
        
       