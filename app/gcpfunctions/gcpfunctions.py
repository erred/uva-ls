from PIL import Image
import flask
import werkzeug.exceptions.InternalServerError
import io
import os
import time
import uuid

SIZE = int(os.getenv("SIZE", "256"))
SERVERID = str(uuid.uuid4())

def handler(request):
    t = time.time_ns()
    tt = time.thread_time_ns()

    post_data = request.get_data()
    im = Image.open(io.BytesIO(post_data))
    im = im.resize((SIZE, SIZE))
    buf = io.BytesIO()
    im.save(buf, format='JPEG')
    buf.seek(0)

    t = time.time_ns() - t
    tt = time.thread_time_ns() - tt

    res = flask.make_response(buf.read())
    res.headers.set("Time", str(t))
    res.headers.set("Thread-Time", str(tt))
    res.headers.set("Server-UUID", SERVERID)
    res.headers.set("Content-Type", 'image/jpeg')
