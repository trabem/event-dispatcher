# Event Dispatcher

This repository contains a pure Python implementation of an event dispatcher. The event dispatcher allows you to create a simple event-driven architecture in your Python applications. It allows you to decouple your application components, making your code cleaner and easier to maintain.

## Features

- Pure Python: No external dependencies.
- Simple API: Easy to understand and use.
- Lightweight: Minimal impact on your application's performance.
- Flexible: Can be used in any Python application.
- Asyncio Support: Compatible with Python's built-in asyncio library.

## Installation

You can install the Event Dispatcher using pip:

```bash
pip install event-dispatching
```

## Usage

Here is a basic example of how to use the Event Dispatcher:

```python
import event_dispatcher

# Create an instance of the Event Dispatcher
dispatcher = event_dispatcher.SyncEventDispatcher()

# Define a callback function
def callback(data):
    print(f"Event received: {data}")

# Register the callback function for the "test" event
dispatcher.subscribe("test", callback)

# Dispatch the "test" event
dispatcher.dispatch("test", "Hello, World!")
```

When you run this code, it will print:

```
Event received: Hello, World!
```
For more examples, please see [examples](https://github.com/trabem/event-dispatcher/tree/main/examples)
## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
