__author__ = 'jeffreytang'

def gen_byte(camera):
    """
    Generator function that yields frames as bytes to display as JPEG
    """
    while True:
        frame = camera.get_display_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def gen_numpy(camera):
    """
    Generator function that yields frames as string of bytes to stream
    """
    while True:
        yield camera.get_numpy_frame()
