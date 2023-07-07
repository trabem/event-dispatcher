import asyncio
from typing import Dict

import event_dispatcher


async def _callback(data: Dict):
    print(data)


async def main():
    event_name = "event.name"

    dispatcher = event_dispatcher.AsyncEventDispatcher()
    dispatcher.subscribe(event_name, _callback)

    await dispatcher.dispatch(event_name, data={"test": "data"})


if __name__ == "__main__":
    asyncio.run(main())
