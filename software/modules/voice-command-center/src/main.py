import sys

sys.dont_write_bytecode = True
import threading

import database.redis as redis_client
import operators.notifier as notifier
import operators.responder as responder
import operators.transcriper as transcriper
import operators.translator as translator
from connection import internet
from database.client import DatabaseClient
from enums.command import CommandEnum


def handle_command(raw_command: str):
    print(raw_command)
    command = translator.translate_command(raw_command)
    if (command == CommandEnum.IDLE): return
    respone = responder.respone(command)
    notifier.notify(respone)

def main():
    redis_instance = redis_client.connect()
    check_connection_thread = threading.Thread(target=internet.start(redis=redis_instance))
    check_connection_thread.start()
    transcriper.start(redis=redis_instance, command=handle_command)
    
if __name__ == "__main__":
    main()