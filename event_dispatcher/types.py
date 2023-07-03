from typing import Any, TypeAlias, Callable, Awaitable

EventData: TypeAlias = Any
SyncCallback: TypeAlias = Callable[[EventData], None]
AsyncCallback: TypeAlias = Callable[[EventData], Awaitable[None]]