from enum import Enum, auto

class PinType(Enum):
    I8 = "int8_t"
    I16 = "int16_t"
    I32 = "int32_t"
    I64 = "int64_t"
    U8 = "uint8_t"
    U16 = "uint16_t"
    U32 = "uint32_t"
    U64 = "uint64_t"
    F32 = "float"
    F64 = "double"
    STR = "t_string"
    BOOL = "bool"
    # UNIT = "void"

    @property
    def to_c(self) -> str:
        return self.value

    def __str__(self) -> str:
        return self.name.lower()