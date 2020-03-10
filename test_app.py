# test_app.py

import pytest
import modules.messenger as m

def test_simple():
    assert True == True


def test_messenger_get_message():
    msg = 'Hello World!'
    messenger = m.Messenger(msg)
    assert messenger.get_message() == msg


