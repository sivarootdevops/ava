import random

from enums.command import CommandEnum


def respone(command: CommandEnum) -> str:
    if (command == CommandEnum.LIGHT_ON):
        responses = [
            "Got it, lights are on!",
            "Sure thing, the room's lit!",
            "Alright, we're shining bright!",
            "light's up!",
            "we're illuminated!",
            "Okay"
        ]
        return random.choice(responses)
    if (command == CommandEnum.LIGHT_OFF):
        responses = [
            "Alright, lights are off!",
            "Sure thing, darkness falls!",
            "Got it, the room's dim!",
            "light's out!",
            "we're in the dark!",
            "Okay"
        ]
        return random.choice(responses)
    responses = [
        "not sure what you mean.",
        "didn't catch that, could you say it again?",
        "didn't quite get that, can you repeat?",
        "didn't follow, can you clarify?",
        "not sure I'm getting it, could you try again?"
    ]
    return random.choice(responses)