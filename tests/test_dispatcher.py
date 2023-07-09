from unittest import mock

from event_dispatcher import SyncEventDispatcher


def test_subscribe_to_event():
    # arrange
    event_name = "test.event_name"
    callback_mock = mock.Mock()
    sut = SyncEventDispatcher()

    # act
    sut.subscribe(event_name, callback_mock)

    # assert
    assert sut.subscribers_count(event_name) == 1
    assert sut.subscribers(event_name)[0] == callback_mock


def test_subscribe_to_event_decorator():
    # arrange
    event_name = "test.event_name"
    callback_mock = mock.Mock()
    sut = SyncEventDispatcher()

    # act
    sut.subscribe(event_name)(callback_mock)

    # assert
    assert sut.subscribers_count(event_name) == 1
    assert sut.subscribers(event_name)[0] == callback_mock


def test_unsubscribe_from_event():
    # arrange
    event_name = "test.event_name"
    callback_mock = mock.Mock()
    sut = SyncEventDispatcher()
    sut.subscribe(event_name, callback_mock)

    # act
    result = sut.unsubscribe(event_name, callback_mock)

    # assert
    assert result == 1


def test_unsubscribe_when_event_does_not_have_subscribers():
    # arrange
    event_name = "test.event_name"
    callback_mock = mock.Mock()
    sut = SyncEventDispatcher()

    # act
    result = sut.unsubscribe(event_name, callback_mock)

    # assert
    assert result == 0


def test_unsubscribe_from_event_no_added_callback():
    # arrange
    event_name = "test.event_name"
    callback_mock = mock.Mock()
    sut = SyncEventDispatcher()
    sut.subscribe(event_name, lambda x: x)

    # act
    result = sut.unsubscribe(event_name, callback_mock)

    # assert
    assert result == 0
