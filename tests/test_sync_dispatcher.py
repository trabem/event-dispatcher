from unittest import mock

from event_dispatcher import SyncEventDispatcher


def test_dispatch_event():
    # arrange
    event_name = "test.event_name"
    event_data = {"test": "data"}
    callback_mock = mock.Mock()
    sut = SyncEventDispatcher()
    sut.subscribe(event_name, callback_mock)

    # act
    result = sut.dispatch(event_name, event_data)

    # assert
    assert result is True
    callback_mock.assert_called_once_with(event_data)


async def test_dispatch_event_without_subscribers():
    # arrange
    event_name = "test.event_name"
    event_data = {"test": "data"}
    sut = SyncEventDispatcher()

    # act
    result = sut.dispatch(event_name, event_data)

    # assert
    assert result is False
