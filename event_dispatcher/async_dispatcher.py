import asyncio

from event_dispatcher import dispatcher, types


class AsyncEventDispatcher(dispatcher.BaseEventDispatcher[types.AsyncCallback]):
    async def dispatch(self, event_name: str, data: types.EventData | None = None) -> None:
        await asyncio.gather(*self._subscribers[event_name])
