from bot.base import Device

import serial

class Arduino(Device):
    def __init__(self, *args, **kwargs):
        self._super = super(Arduino, self)
        self._super.__init__(*args, **kwargs)

    def connect(self):
        if not self.connected:
            self.connector = serial.Serial(self.device_id)
        return self

    def disconnect(self):
        
        return self