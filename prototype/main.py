from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable

from norm import NormEnum, NormError
from pin_type import PinType
from pin_value import PinUnit, PinValue


@dataclass(frozen=True)
class PinExpression:
    """
    something like a = 3 + 2 * 3
    Pin will ignore after =, C code will handle that
    """

    ...


@dataclass(frozen=True)
class PinParam:
    body: list[PinValue] = field(default_factory=list)

    def __post_init__(self):
        if len(self.body) > NormEnum.MAX_NUM_PARAMETERS:
            raise NormError(
                f"cannot have more than {NormEnum.MAX_NUM_PARAMETERS} parameters"
            )

    def __param_conversion(self, func: Callable[[PinValue], str]) -> str:
        return "(" + ", ".join(map(func, self.body)) + ")"

    @property
    def is_unit(self) -> bool:
        return len(self.body) == 0

    def __repr__(self) -> str:
        if self.is_unit:
            return "unit"
        return self.__param_conversion(lambda x: f"{x.name}: {x.type_}")

    @property
    def to_c(self) -> str:
        if self.is_unit:
            return "void"
        return self.__param_conversion(lambda x: f"{x.type_.to_c} {x.name}")


@dataclass(frozen=True)
class PinFuncVarDecl:
    variables: list[PinValue] = field(default_factory=list)

    def __post_init__(self):
        if len(self.variables) > NormEnum.MAX_NUM_VARIABLES:
            raise NormError(
                f"cannot have more than {NormEnum.MAX_NUM_VARIABLES} variables"
            )

    def __repr__(self) -> str:
        return " ".join(map(lambda x: f"{x.name}: {x.type_}", self.variables))


@dataclass(frozen=True)
class PinFunc:
    name: str
    param: PinParam = field(default_factory=PinParam)
    returns: PinType | PinUnit = PinUnit()
    variables: PinFuncVarDecl = field(default_factory=PinFuncVarDecl)
    body: list[PinExpression] = field(default_factory=list)

    def __repr__(self) -> str:
        body = f"{self.name} :: fn{self.param} -> {self.returns} {{\n"
        body += str(self.variables)  # TODO
        body += str(self.body)  # TODO
        body += "\n}\n"
        return body

    @property
    def to_c(self) -> str:
        body = f"{self.returns.to_c}\t{self.name}{self.param.to_c}\n{{\n"
        body += f"{self.variables}\n"  # TODO
        body += f"{self.body}\n"  # TODO
        body += "\n}\n"
        return body


hello = PinValue("spam", PinType.STR, "hello")
world = PinValue("egg", PinType.STR, "world")
param = PinParam([hello, world])
vardecl = PinFuncVarDecl([hello, world])
print(param.to_c)
func = PinFunc(
    name="main", param=param, returns=PinType.I32, variables=vardecl
)

print(func)
print(func.to_c)

file = Path("test.c")
file.write_text(func.to_c)
# expression: dict

# test = Macro(name="print!", args=["{hello} {world}"])


# def compile_macro_print():
#     """
#     before: print!("{hello} {world}")
#     after : printf("%s %s", hello, world);
#     """
