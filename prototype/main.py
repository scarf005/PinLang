from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Any, Callable


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
    UNIT = "void"

    @property
    def to_c(self) -> str:
        return self.value

    def __str__(self) -> str:
        return self.name.lower()


@dataclass(frozen=True)
class PinValue:
    name: str
    type_: PinType
    value: Any
    const: bool = True


@dataclass(frozen=True)
class PinExpression:
    """
    something like a = 3 + 2 * 3
    pin will ignore after =, C code will handle that
    """

    ...


@dataclass(frozen=True)
class PinParam:
    body: list[PinValue] = field(default_factory=list)

    def __post_init__(self):
        if len(self.body) == 0:
            body = [PinValue(name="", type_=PinType.UNIT, value="")]
        elif len(self.body) > 4:
            raise ValueError("PinParam must have at most 4 values")

    def __param_conversion(self, func: Callable[[PinValue], str]) -> str:
        return "(" + ", ".join(map(func, self.body)) + ")"

    def __repr__(self) -> str:
        return self.__param_conversion(lambda x: f"{x.name}: {x.type_}")

    @property
    def to_c(self) -> str:
        return self.__param_conversion(lambda x: f"{x.type_.to_c} {x.name}")
        return "(" + ", ".join([x.to_c_param for x in self.body]) + ")"


@dataclass(frozen=True)
class PinFunction:
    name: str
    param: PinParam = field(default_factory=PinParam)
    returns: PinType = PinType.UNIT
    variables: list[PinValue] = field(default_factory=list)
    body: list[PinExpression] = field(default_factory=list)

    def __repr__(self) -> str:
        body = f"{self.name} :: fn{self.param} -> {self.returns} {{\n"
        body += str(self.body)  # TODO
        body += "}\n"
        return body

    @property
    def to_c(self) -> str:
        body = f"{self.returns.to_c}\t{self.name}({self.param})\n{{\n"
        body += str(self.body)  # TODO
        body += "}\n"
        return body


@dataclass
class PinMacro:
    name: str
    args: list[str]


"foo := 10"
"bar :: 20"

hello = PinValue("spam", PinType.STR, "hello")
world = PinValue("egg", PinType.STR, "world")
param = PinParam([hello, world])
print(param.to_c)
func = PinFunction(
    name="main", param=param, returns=PinType.I32, variables=[hello, world]
)

# print(hello)
print(func)
# print(func.to_c())
# expression: dict

# test = Macro(name="print!", args=["{hello} {world}"])


# def compile_macro_print():
#     """
#     before: print!("{hello} {world}")
#     after : printf("%s %s", hello, world);
#     """
