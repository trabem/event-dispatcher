"""Async implementation of event dispatcher

This module provide async implementation for BaseEventDispatcher.
Implementation based on standard asyncio library.
All callbacks are executes concurrently with `asyncio.gather`.
It means callbacks sequential execution don't guaranteed.

Typical usage example:

  dispatcher = AsyncEventDispatcher()
  dispatcher.subscribe("event.name", async_callback)
  await dispatcher.dispatch("event.name", {"event": "data"})
"""

import asyncio

from event_dispatcher import _dispatcher, types


class AsyncEventDispatcher(_dispatcher.BaseEventDispatcher[types.AsyncCallback]):
    async def dispatch(
        self, event_name: str, data: types.EventData | None = None
    ) -> bool:
        subscribers = self._subscribers[event_name]

        if not subscribers:
            return False

        await asyncio.gather(*[callback(data) for callback in subscribers])

        return True
