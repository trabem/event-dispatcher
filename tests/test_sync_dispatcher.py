from unittest.mock import Mock

from event_dispatcher import SyncEventDispatcher


def test_subscribe_callback():
    # arrange
    event_name = "test.event_name"
    callback_mock = Mock()
    sut = SyncEventDispatcher()

    # act
    sut.subscribe(event_name, callback_mock)

    # assert
    assert sut.subscribers_count(event_name) == 1
    assert sut.subscribers(event_name)[0] == callback_mock
