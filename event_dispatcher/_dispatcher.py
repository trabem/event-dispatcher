"""Contains basic class for all implementation event dispatchers

This module is meant for internal usage, not for users of the library.
If you want implement custom event dispatcher
use `event_dispatcher.BaseEventDispatcher`
"""

import collections
from abc import ABC, abstractmethod
from typing import Callable, Generic, List, Optional, TypeVar

from event_dispatcher import types

_CallbackT = TypeVar("_CallbackT", covariant=True)


class BaseEventDispatcher(ABC, Generic[_CallbackT]):
    def __init__(self):
        self._subscribers = collections.defaultdict(list)

    def subscribe(self, event_name: str, callback: _CallbackT) -> None:
        self._subscribers[event_name].append(callback)

    def subscribe_decorator(
        self, event_name: str
    ) -> Callable[[_CallbackT], _CallbackT]:
        def decorator(callback: _CallbackT) -> _CallbackT:
            self.subscribe(event_name, callback)
            return callback

        return decorator

    def subscribers_count(self, event_name: str) -> int:
        return len(self._subscribers[event_name])

    def subscribers(self, event_name: str) -> List[_CallbackT]:
        return self._subscribers[event_name].copy()

    def unsubscribe(self, event_name, callback: _CallbackT) -> int:
        event_subscribers = self._subscribers[event_name]
        if not event_subscribers:
            return 0

        total_removed = 0
        event_subscribers_idx = len(event_subscribers) - 1

        while event_subscribers_idx >= 0:
            if event_subscribers[event_subscribers_idx] == callback:
                del event_subscribers[event_subscribers_idx]
                total_removed += 1

            event_subscribers_idx -= 1
        return total_removed

    @abstractmethod
    def dispatch(
        self, event_name: str, data: Optional[types.EventData] = None
    ) -> bool:  # pragma: no cover
        pass
