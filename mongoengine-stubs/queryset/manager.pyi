from typing import (
    Any,
    Self,
    TypeVar,
    Type,
    overload,
    Generic,
    Protocol,
)

from mongoengine.queryset.queryset import QuerySet

T = TypeVar("T")

class _GetQuerySet(Protocol[T]):
    @overload
    def __call__(self, queryset: QuerySet[T]) -> QuerySet[T]: ...
    @overload
    def __call__(
        self, owner: Type[T], queryset: QuerySet[T], *args: Any, **kwargs: Any
    ) -> QuerySet[T]: ...

class QuerySetManager(Generic[T]):
    get_queryset: _GetQuerySet[T] | None
    default: QuerySet[T] | None = ...

    def __init__(self, queryset_func: _GetQuerySet[Any] | None = ...) -> None: ...
    @overload
    def __get__(self, instance: None, owner: Type[T]) -> Self: ...
    @overload
    def __get__(self, instance: Any, owner: Type[T]) -> QuerySet[T]: ...

def get_queryset(func: _GetQuerySet[T]) -> QuerySetManager[T]: ...
