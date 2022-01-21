from __future__ import absolute_import

from bot.base           import ConnectableObject
from bot.camera.webcam  import WebCamera
from bot.connection     import Connection
from bot.motion         import Controller as MotionController
from bot.face           import FaceRecognizer
from bot.screen         import Screen

class Bot(ConnectableObject):
    def __init__(self):
        self._connection    = Connection()
        self._screen        = Screen()
        self._camera        = WebCamera()
        self._motion        = MotionController()
        self._face          = FaceRecognizer()

    @property
    def camera(self):
        return getattr(self, "_camera", None)

    def connect(self):
        return self._connection.connect()

    def close(self):
        return self._connection.close()