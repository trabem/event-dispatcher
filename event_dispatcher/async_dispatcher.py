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
