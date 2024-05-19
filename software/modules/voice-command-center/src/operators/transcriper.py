from typing import Callable

from enums.redis import StateKeyEnum, StatusEnum
from redis import Redis
from speech_recognition import (Microphone, Recognizer, RequestError,
                                UnknownValueError, WaitTimeoutError)


def start(command: Callable[[str], None], redis: Redis, timeout: int = 3, phrase_time_limit: int = 3, ) -> None:
    recognizer = Recognizer()
    while True:
        if (redis.get(StateKeyEnum.INTERNET_STATUS) == StatusEnum.OFFLINE): continue
        with Microphone() as source:
            try:
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
                try:
                    command(recognizer.recognize_google(audio))
                except UnknownValueError as e:
                    print("Sorry, I could not understand what you said.")
                except RequestError as e:
                    print("Could not request results from Google Speech Recognition service; {0}".format(e))
            except WaitTimeoutError as e:
                print("error {0}".format(e))
                continue