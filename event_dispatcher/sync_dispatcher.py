from event_dispatcher import _dispatcher, types


class SyncEventDispatcher(_dispatcher.BaseEventDispatcher[types.SyncCallback]):
    def dispatch(self, event_name: str, data: types.EventData | None = None) -> bool:
        subscribers = self._subscribers[event_name]

        if not subscribers:
            return False

        for subscriber in subscribers:
            subscriber(data)

        return True
