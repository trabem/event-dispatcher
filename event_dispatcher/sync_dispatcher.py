"""Sync implementation of event dispatcher

This module provide sync implementation for BaseEventDispatcher.
All callbacks are executed sequentially and callbacks sequential execution is guaranteed.

Typical usage example:

  dispatcher = SyncEventDispatcher()
  dispatcher.subscribe("event.name", async_callback)
  dispatcher.dispatch("event.name", {"event": "data"})
"""
from typing import Optional

from event_dispatcher import _dispatcher, types


class SyncEventDispatcher(_dispatcher.BaseEventDispatcher[types.SyncCallback]):
    def dispatch(self, event_name: str, data: Optional[types.EventData] = None) -> bool:
        subscribers = self._subscribers[event_name]

        if not subscribers:
            return False

        for subscriber in subscribers:
            subscriber(data)

        return True
