from enums.command import CommandEnum


def translate_command(raw_command: str) -> CommandEnum:
    if (search(raw_command, "light") and search(raw_command, "on")):
        return CommandEnum.LIGHT_ON
    if (search(raw_command, "light") and search(raw_command, "off")):
        return CommandEnum.LIGHT_OFF
    if (search(raw_command, "Sophia")):
        return CommandEnum.NOT_UNDERSTAND
    else:
        return CommandEnum.IDLE

def search(text: str, search: str) -> bool:
    return text.find(search) != -1