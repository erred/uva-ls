from PIL import Image
# import http.server
import flask
import werkzeug.exceptions.InternalServerError
import io
import os
# import socketserver
import time
import uuid

SIZE = int(os.getenv("SIZE", "256"))
# PORT = int(os.getenv("PORT", "8080"))
SERVERID = uuid.uuid4()

def handler(request):
    try:
        t = time.time_ns()
        tt = time.thread_time_ns()

        post_data = request.get_data()
        im = Image.open(io.BytesIO(post_data))
        im = im.resize((SIZE, SIZE))
        buf = io.BytesIO()
        im.save(buf, format='jpeg')
        buf.seek(0)

        t = time.time_ns() - t
        tt = time.thread_time_ns() - tt

        res = flask.make_response(buf.read())
        res.headers.set("Time", str(t))
        res.headers.set("Thread-Time", str(tt))
        res.headers.set("Server-UUID", SERVERID)
    except Exception as e:
        flask.abort(500, str(e))
