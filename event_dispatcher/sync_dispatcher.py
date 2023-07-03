from event_dispatcher import dispatcher, types


class SyncEventDispatcher(dispatcher.BaseEventDispatcher[types.SyncCallback]):
    def dispatch(self, event_name: str, data: types.EventData | None = None) -> None:
        for subscriber in self._subscribers[event_name]:
            subscriber(data)
