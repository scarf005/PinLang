from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable

import deal

from norm import TAB_N, NormEnum
from pin_const import TAB_P, PinEnum
from pin_type import PinType
from pin_value import PinUnit, PinValue


@dataclass(frozen=True)
class PinExpr:
    """
    something like a = 3 + 2 * 3
    Pin will ignore after =, C code will handle that
    """

    ...


@dataclass(frozen=True)
class PinParam:
    body: list[PinValue] = field(default_factory=list)

    def __post_init__(self):
        assert (
            len(self.body) <= NormEnum.MAX_NUM_PARAMETERS
        ), f"cannot have more than {NormEnum.MAX_NUM_PARAMETERS} parameters"

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


@dataclass
class PinFuncVarDecl:
    variables: list[PinValue] = field(default_factory=list)

    def __post_init__(self):
        assert (
            len(self.variables) <= NormEnum.MAX_NUM_VARIABLES
        ), f"cannot have more than {NormEnum.MAX_NUM_VARIABLES} variables"
        self.type_longest: int = len(
            max(self.variables, key=lambda x: len(x.type_.to_c)).type_.to_c
        )

    def __repr__(self) -> str:
        return "\n".join(
            [f"{TAB_P}{x.name}: {x.type_}" for x in self.variables]
        )

    @property
    def to_c(self) -> str:
        return "\n".join(
            [f"{TAB_N}{x.type_.to_c}{TAB_N}{x.name};" for x in self.variables]
        )


@dataclass
class PinFunc:
    name: str
    param: PinParam = field(default_factory=PinParam)
    returns: PinType | PinUnit = PinUnit()
    variables: PinFuncVarDecl = field(default_factory=PinFuncVarDecl)
    body: list[PinExpr] = field(default_factory=list)

    def __repr__(self) -> str:
        body = f"{self.name} :: fn{self.param} -> {self.returns} {{\n"
        body += f"{self.variables}\n"  # TODO
        body += f"{self.body}\n"  # TODO
        body += "\n}\n"
        return body

    @property
    def to_c(self) -> str:
        body = f"{self.returns.to_c}\t{self.name}{self.param.to_c}\n{{\n"
        body += f"{self.variables.to_c}\n"  # TODO
        body += f"{self.body}\n"  # TODO
        body += "\n}\n"
        return body


hello = PinValue("spam", PinType.STR, "hello")
world = PinValue("egg", PinType.STR, "world")
param = PinParam([hello, world])
vardecl = PinFuncVarDecl([hello, world])

func = PinFunc(
    name="test", param=param, returns=PinType.I32, variables=vardecl
)

print(vardecl.type_longest)
print(vardecl.to_c)

print(func)
print(func.to_c)

class PinRange:
    ...

class PinFor(PinExpr):
    """
        for {(...)} => while (true) {(...)}
        for (condition) {(...)} => while (condition) {(...)}
        for 0..10 {(...)} => int i; i = -1; while (++i < 10) {(...)}
    """
    body: list[PinExpr] = field(default_factory=list)

    def __repr__(self) -> str:
        ...

# file = Path("test.c")
# file.write_text('#include "pin.h"\n\n' + func.to_c)
# expression: dict

# test = Macro(name="print!", args=["{hello} {world}"])


# def compile_macro_print():
#     """
#     before: print!("{hello} {world}")
#     after : printf("%s %s", hello, world);
#     """
