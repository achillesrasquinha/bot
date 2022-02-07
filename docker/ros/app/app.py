from flask import Flask
from flask_socketio import SocketIO

import serial

app     = Flask(__name__)
socket  = SocketIO(app)



@socket.on("connect")
def connect():
    print("A user is connected.")

@app.route("/")
def index():
    return "<h1>HTTP Socket Server</h1>"

if __name__ == "__main__":
    socket.run(app)