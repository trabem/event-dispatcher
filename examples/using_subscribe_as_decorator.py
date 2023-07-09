import event_dispatcher


def main():
    event_name = "event.name"

    dispatcher = event_dispatcher.SyncEventDispatcher()

    @dispatcher.subscribe(event_name)
    def _callback(data):
        print(data)

    dispatcher.dispatch(event_name, {"test": "data"})


if __name__ == "__main__":
    main()
