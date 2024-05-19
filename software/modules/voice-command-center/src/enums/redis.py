from enum import Enum


class StateKeyEnum(str, Enum):
    INTERNET_STATUS = "INTERNET_STATUS"

class StatusEnum(str, Enum):
    ONLINE = "ONLINE"
    OFFLINE = "OFFLINE"