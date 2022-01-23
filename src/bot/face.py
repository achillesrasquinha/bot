from deepface import DeepFace

from bot.base import Object

class FaceRecognizer(Object):
    def recognize(self, array):
        DeepFace.detectFace(array)