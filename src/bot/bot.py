from __future__ import absolute_import

from bot.connection import Connection

class Bot:
    def connect(self):
        self.connection = Connection()

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self):
        self.disconnect()
        return self