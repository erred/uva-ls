from PIL import Image
import base64
import io
import os
import time
import uuid

SIZE = int(os.getenv("SIZE", "256"))
SERVERID = str(uuid.uuid4())

def handler(event, context):
    try:
        st0 = time.clock_gettime(time.CLOCK_REALTIME)
        tt0 = time.clock_getres(time.CLOCK_THREAD_CPUTIME_ID)

        post_data = base64.b64decode(event["body"])

        st1 = time.clock_gettime(time.CLOCK_REALTIME)
        tt1 = time.clock_getres(time.CLOCK_THREAD_CPUTIME_ID)

        im = Image.open(io.BytesIO(post_data))
        im = im.resize((SIZE, SIZE))
        buf = io.BytesIO()
        im.save(buf, format='JPEG')

        st2 = time.clock_gettime(time.CLOCK_REALTIME)
        tt2 = time.clock_getres(time.CLOCK_THREAD_CPUTIME_ID)

        buf.seek(0)
        buffed = base64.b64encode(buf.read()).decode("UTF-8")

        st3 = time.clock_gettime(time.CLOCK_REALTIME)
        tt3 = time.clock_getres(time.CLOCK_THREAD_CPUTIME_ID)

        res = {
            "statusCode": 200,
            "headers": {
                "Time": ', '.join(map(str, [st1-st0, st2-st1, st3-st2])),
                "Thread-Time": ', '.join(map(str, [tt1-tt0, tt2-tt1, tt3-tt2])),
                "Server-UUID": SERVERID,
                "Content-Type": "image/jpeg",
            },
            "isBase64Encoded": True,
            "body": buffed,
        }
    except Exception as e:
        res = {
            "statusCode": 500,
            "headers": {
                "Server-UUID": SERVERID,
            }
            "body": str(e)
        }
    return res
