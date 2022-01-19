

# imports - module imports
from bot.exception import (
    BotError
)

# imports - test imports
import pytest

def test_bot_error():
    with pytest.raises(BotError):
        raise BotError