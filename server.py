#!/usr/bin/python
from gevent import monkey
monkey.patch_all()

from flask import Flask, render_template
from flask.ext.socketio import SocketIO, emit
from camera import Camera
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('channel-a')
def channel_a(message):
    """
    Receives a message, on `channel-a`, and emits to the same channel.
    """
    print "[x] Received\t: ", message
    emit_message('Hi I am a server')
    emit_frame(Camera())


def emit_message(message, n_char=100):
    emit("channel-a", message)
    print "[x] Sent\t: ", message[:n_char]

def emit_frame(camera):
    """
    Generator function that yields frames as string of bytes to stream
    """
    success = True
    while success:
        success, img_np_str = camera.get_numpy_frame()
        emit_message(img_np_str)
        time.sleep(0.1)

if __name__ == '__main__':
    app.debug = True
    socketio.run(app, port=3000)

