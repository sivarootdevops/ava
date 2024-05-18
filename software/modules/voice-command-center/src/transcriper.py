from typing import Callable

from speech_recognition import (Microphone, Recognizer, RequestError,
                                UnknownValueError, WaitTimeoutError)


class Transcriper:
    def __init__(self, command: Callable[[str], None], timeout: int = 3, phrase_time_limit: int = 3):
        self.recognizer = Recognizer()
        self.command = command
        self.timeout = timeout
        self.phrase_time_limit = phrase_time_limit
        
    def start(self) -> None:
        while True:
            with Microphone() as source:
                try:
                    self.recognizer.adjust_for_ambient_noise(source)
                    audio = self.recognizer.listen(source, timeout=self.timeout, phrase_time_limit=self.phrase_time_limit)
                    try:
                        self.command(self.recognizer.recognize_google(audio))
                    except UnknownValueError as e:
                        print("Sorry, I could not understand what you said.")
                    except RequestError as e:
                        print("Could not request results from Google Speech Recognition service; {0}".format(e))
                except WaitTimeoutError as e:
                    print("error {0}".format(e))
                    continue