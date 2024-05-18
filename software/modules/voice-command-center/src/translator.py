from enums.command import CommandEnum


class Translator:
    def translate_command(self, raw_command: str) -> CommandEnum:
        if (self.search(raw_command, "light") and self.search(raw_command, "on")):
            return CommandEnum.LIGHT_ON
        if (self.search(raw_command, "light") and self.search(raw_command, "off")):
            return CommandEnum.LIGHT_OFF
        if (self.search(raw_command, "Sophia")):
            return CommandEnum.NOT_UNDERSTAND
        else:
            return CommandEnum.IDLE
        
        
    def search(self,text: str, search: str) -> bool:
        return text.find(search) != -1