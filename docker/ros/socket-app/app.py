from flask import Flask
from flask_socketio import SocketIO

import serial
import serial.threaded

from bpyutils.util.environ import getenv
from bpyutils.util.system  import popen
from bpyutils.exception    import PopenError

app     = Flask(__name__)
socket  = SocketIO(app)

class SerialToSocketIO(serial.threaded.Protocol):
    def __init__(self, *args, **kwargs):
        self._super = super(SerialToSocketIO, self)
        self._super.__init__(*args, **kwargs)

    def __call__(self):
        return self

    def data_received(self, data):
        socket.emit("serial:data", data)

@socket.on("connect")
def connect():
    print("A user is connected.")

@socket.on("data")
def on_data(data):
    try:
        popen("socat pty,link='/dev/tty.Bridge-Port' tcp:ros:7777")
    except PopenError:
        print("Error using socat")

@app.route("/")
def index():
    return "<h1>HTTP Socket Server</h1>"

if __name__ == "__main__":
    _serial = serial.serial_for_url("/dev/tty.Bridge-Port")
    _serial.baudrate = 115200

    try:
        _serial.open()

        serial_sio    = SerialToSocketIO()
        serial_worker = serial.threaded.ReaderThread(_serial, serial_sio)
    except:
        print("Unable to open bridge port.")

    socket.run(app)