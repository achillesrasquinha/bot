from PIL import Image

class CameraImage:
    def __init__(self, arr):
        self._array = arr
        self._pil   = Image.fromarray(arr)

    def show(self):
        return self._pil.show()
