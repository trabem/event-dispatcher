import event_dispatcher


def _callback(data):
    print(data)


def main():
    event_name = "event.name"

    dispatcher = event_dispatcher.SyncEventDispatcher()

    dispatcher.subscribe(event_name, _callback)
    dispatcher.dispatch(event_name, {"test": "data"})  # executed callback `_callback`

    dispatcher.unsubscribe(event_name, _callback)
    dispatcher.dispatch(
        event_name, {"test": "data"}
    )  # doesnt executed callback `_callback`


if __name__ == "__main__":
    main()
