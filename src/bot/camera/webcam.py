from bot.camera import Camera
from bot.camera.image import CameraImage

class WebCamera(Camera):
    """
        A computer web-camera interface for development.
    """
    def __init__(self, device_id = 0, *args, **kwargs):
        self._super     = super(WebCamera, self)
        self._super.__init__(module = {
            "package": "cv2", "name": "opencv-python"
        }, *args, **kwargs)

        self._device_id = device_id
        
    def connect(self):
        if not self._capture:
            self._capture = self._module.VideoCapture(self._device_id)
        return self

    def close(self):
        if self._capture:
            self._capture.release()

    def snap(self):
        if self.connected:
            retval, frame = self._capture.read()
            image = CameraImage(frame)

            return image