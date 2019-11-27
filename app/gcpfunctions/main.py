from PIL import Image
import flask
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

    return (buf.read(), 200, {
        "Time": str(t),
        "Thread-Time": str(tt),
        "Server-UUID": SERVERID,
        "Content-Type": "image/jpeg",
    })
