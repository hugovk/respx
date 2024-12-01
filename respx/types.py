from collections.abc import (
    AsyncIterable,
    Awaitable,
    Iterable,
    Iterator,
    Mapping,
    Sequence,
)
from re import Pattern
from typing import IO, Any, Callable, Optional, TypeVar, Union

import httpx

URL = tuple[
    bytes,  # scheme
    bytes,  # host
    Optional[int],  # port
    bytes,  # path
]
Headers = list[tuple[bytes, bytes]]
Content = Union[str, bytes, Iterable[bytes], AsyncIterable[bytes]]

HeaderTypes = Union[
    httpx.Headers,
    dict[str, str],
    dict[bytes, bytes],
    Sequence[tuple[str, str]],
    Sequence[tuple[bytes, bytes]],
]
CookieTypes = Union[dict[str, str], Sequence[tuple[str, str]]]

DefaultType = TypeVar("DefaultType", bound=Any)

URLPatternTypes = Union[str, Pattern[str], URL, httpx.URL]
QueryParamTypes = Union[
    bytes, str, list[tuple[str, Any]], dict[str, Any], tuple[tuple[str, Any], ...]
]

ResolvedResponseTypes = Optional[Union[httpx.Request, httpx.Response]]
RouteResultTypes = Union[ResolvedResponseTypes, Awaitable[ResolvedResponseTypes]]
CallableSideEffect = Callable[..., RouteResultTypes]
SideEffectListTypes = Union[httpx.Response, Exception, type[Exception]]
SideEffectTypes = Union[
    CallableSideEffect,
    Exception,
    type[Exception],
    Iterator[SideEffectListTypes],
]

# Borrowed from HTTPX's "private" types.
FileContent = Union[IO[bytes], bytes, str]
FileTypes = Union[
    # file (or bytes)
    FileContent,
    # (filename, file (or bytes))
    tuple[Optional[str], FileContent],
    # (filename, file (or bytes), content_type)
    tuple[Optional[str], FileContent, Optional[str]],
    # (filename, file (or bytes), content_type, headers)
    tuple[Optional[str], FileContent, Optional[str], Mapping[str, str]],
]
RequestFiles = Union[Mapping[str, FileTypes], Sequence[tuple[str, FileTypes]]]
