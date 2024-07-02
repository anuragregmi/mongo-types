from typing import Self, Literal, Any

__all__ = ("QueryFieldList",)

class QueryFieldList:
    ONLY: Literal[1] = ...
    EXCLUDE: Literal[0] = ...

    value: Literal[1,0]
    fields: set[str]
    always_include: set[str]
    _id: Any|None
    _only_called: bool
    slice: dict[str, Literal[1,0]]

    def __init__(
        self,
        fields: list[str] | None = ...,
        value: Literal[1,0] = ...,
        always_include: list[str] | None = ...,
        _only_called: bool = ...,
    ) -> None: ...
    def __add__(self, f: Self) -> Self: ...
    def __bool__(self) -> bool: ...
    def as_dict(self) -> dict[str, Any]