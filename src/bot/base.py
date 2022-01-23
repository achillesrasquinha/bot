class Object(object):
    pass
class ConnectableObject(Object):
    def __init__(self, *args, **kwargs):
        self._super     = super(ConnectableObject, self)
        self._super.__init__(*args, **kwargs)

        self._connector = None

    @property
    def connector(self):
        value = getattr(self, "_connector", None)
        return value

    @connector.setter
    def connector(self, value):
        self._connector = value

    def connected(self):
        connector = self.connector
        return bool(connector)

    def connect(self):
        raise NotImplementedError

    def close(self):
        raise NotImplementedError

    def __enter__(self):
        return self.connect()

    def __exit__(self, exc_type, exc_value, tb):
        return self.close()

class Device(ConnectableObject):
    def __init__(self, device_id = None, *args, **kwargs):
        self._super = super(Device, self)
        self._super.__init__(*args, **kwargs)

        self._device_id = device_id

    @property
    def device_id(self):
        return getattr(self, "_device_id", None)