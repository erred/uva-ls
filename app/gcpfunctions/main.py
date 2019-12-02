from PIL import Image
import flask
import io
import os
import time
import uuid

SIZE = int(os.getenv("SIZE", "256"))
SERVERID = str(uuid.uuid4())

def handler(request):
    try:
        st0 = time.clock_gettime(time.CLOCK_REALTIME)
        tt0 = time.clock_gettime(time.CLOCK_THREAD_CPUTIME_ID)

        post_data = request.get_data()

        st1 = time.clock_gettime(time.CLOCK_REALTIME)
        tt1 = time.clock_gettime(time.CLOCK_THREAD_CPUTIME_ID)

        im = Image.open(io.BytesIO(post_data))
        im = im.resize((SIZE, SIZE))
        buf = io.BytesIO()
        im.save(buf, format='JPEG')

        st2 = time.clock_gettime(time.CLOCK_REALTIME)
        tt2 = time.clock_gettime(time.CLOCK_THREAD_CPUTIME_ID)

        buf.seek(0)
        buf.read()

        st3 = time.clock_gettime(time.CLOCK_REALTIME)
        tt3 = time.clock_gettime(time.CLOCK_THREAD_CPUTIME_ID)

        buf.seek(0)
        res = (buf.read(), 200, {
            "Time": ', '.join([str(int(1000000000 * x)) for x in [st1-st0, st2-st1, st3-st2]]),
            "Thread-Time": ', '.join([str(int(1000000000 * x)) for x in [tt1-tt0, tt2-tt1, tt3-tt2]]),
            "Server-UUID": SERVERID,
            "Content-Type": "image/jpeg",
        })
    except Exception as e:
        res = (str(e), 500, {
            "Server-UUID": SERVERID
        })
    return res
