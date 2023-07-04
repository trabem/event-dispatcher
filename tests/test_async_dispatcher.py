from unittest import mock

from event_dispatcher import AsyncEventDispatcher


async def test_dispatch_event():
    # arrange
    event_name = "test.event_name"
    event_data = {"test": "data"}
    callback_mock = mock.AsyncMock()
    sut = AsyncEventDispatcher()
    sut.subscribe(event_name, callback_mock)

    # act
    result = await sut.dispatch(event_name, event_data)

    # assert
    assert result is True
    callback_mock.assert_called_once_with(event_data)


async def test_dispatch_event_without_subscribers():
    # arrange
    event_name = "test.event_name"
    event_data = {"test": "data"}
    sut = AsyncEventDispatcher()

    # act
    result = await sut.dispatch(event_name, event_data)

    # assert
    assert result is False
