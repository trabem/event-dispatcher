import dataclasses
from typing import Dict

import event_dispatcher


@dataclasses.dataclass
class EventData:
    data: Dict


def _callback(data: EventData):
    print(data)


def main():
    event_name = "event.name"

    dispatcher = event_dispatcher.SyncEventDispatcher()
    dispatcher.subscribe(event_name, _callback)

    event_data = EventData(data={"test": "data"})
    dispatcher.dispatch(event_name, event_data)


if __name__ == "__main__":
    main()
