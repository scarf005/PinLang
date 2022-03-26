from enum import IntEnum

class NormEnum(IntEnum):
    MAX_NUM_PARAMETERS = 4
    MAX_NUM_VARIABLES = 5

class NormError(Exception):
    ...