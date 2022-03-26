from dataclasses import dataclass, field
from typing import Any, Type

from norm import NormError
from pin_type import PinType


@dataclass(frozen=True)
class PinValue:
    name: str
    type_: PinType
    value: Any
    const: bool = True

    def __str__(self) -> str:
        if self.const:
            return f"{self.name} : {self.type_} : {self.value}"
        elif self.value is not None:
            return f"{self.type_} : {self.name} : {self.value}"
        return f"{self.name}: {self.type_}"

    @property
    def to_c(self) -> Type[NormError]:
        raise NormError(
            "Norm requires variables to be aligned inside function, "
            "hence this functionality should be handled in PinFuncVarDecl"
        )


class PinUnit:
    def __str__(self) -> str:
        return "unit"

    @property
    def to_c(self) -> str:
        return "void"
