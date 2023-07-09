"""types for event dispatcher"""

from typing import Any, Awaitable, Callable

EventData = Any
SyncCallback = Callable[[EventData], None]
AsyncCallback = Callable[[EventData], Awaitable[None]]
