class Object:
    pass

class ConnectableObject(Object):
    def connect(self):
        raise NotImplementedError

    def close(self):
        raise NotImplementedError

    def __enter__(self):
        return self.connect()

    def __exit__(self, exc_type, exc_value, tb):
        return self.close()