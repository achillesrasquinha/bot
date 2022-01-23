import time

from bot.util.environ import getenv
from bot.ware import Arduino

if __name__ == "__main__":
    port    = getenv("PORT_ARDUINO")
    arduino = Arduino(port)

