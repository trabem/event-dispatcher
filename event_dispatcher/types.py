"""types for event dispatcher"""

from typing import Any, Awaitable, Callable, TypeAlias

EventData: TypeAlias = Any
SyncCallback: TypeAlias = Callable[[EventData], None]
AsyncCallback: TypeAlias = Callable[[EventData], Awaitable[None]]
