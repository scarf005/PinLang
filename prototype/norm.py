from enum import IntEnum


class NormEnum(IntEnum):
    MAX_NUM_PARAMETERS = 4
    MAX_NUM_VARIABLES = 5
    TAB_SIZE = 4

TAB_N =  " " *  NormEnum.TAB_SIZE

class NormError(Exception):
    ...
