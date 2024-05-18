import sys

sys.dont_write_bytecode = True

from enums.command import CommandEnum
from notifier import Notifier
from responder import Responder
from transcriper import Transcriper
from translator import Translator


def handle_command(raw_command: str):
    command = Translator().translate_command(raw_command)
    if (command == CommandEnum.IDLE): return
    respone = Responder().respone(command)
    Notifier().notify(respone)

def main():
    transcriper = Transcriper(command=handle_command).start()
    
if __name__ == "__main__":
    main()