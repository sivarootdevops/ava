import random

from enums.command import CommandEnum


class Responder:        
    def respone(self, command: CommandEnum) -> str:
        if (command == CommandEnum.LIGHT_ON):
            responses = [
                "Got it, lights are on!",
                "Sure thing, the room's lit!",
                "Alright, we're shining bright!",
                "Roger that, light's up!",
                "Copy that, we're illuminated!"
            ]
            return random.choice(responses)
        if (command == CommandEnum.LIGHT_OFF):
            responses = [
                "Alright, lights are off!",
                "Sure thing, darkness falls!",
                "Got it, the room's dim!",
                "Roger that, light's out!",
                "Copy that, we're in the dark!"
            ]
            return random.choice(responses)
        responses = [
            "Oops, not sure what you mean.",
            "Hmm, didn't catch that, could you say it again?",
            "Ah, didn't quite get that, can you repeat?",
            "Sorry, didn't follow, can you clarify?",
            "Hmm, not sure I'm getting it, could you try again?"
        ]
        return random.choice(responses)