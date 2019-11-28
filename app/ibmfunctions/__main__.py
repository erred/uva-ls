from PIL import Image
import base64
import io
import os
import time
import uuid

SIZE = int(os.getenv("SIZE", "256"))
# PORT = int(os.getenv("PORT", "8080"))
SERVERID = str(uuid.uuid4())

def main(args):
    try:
        t = time.time_ns()
        tt = time.thread_time_ns()

        post_data = base64.b64decode(args["__ow_body"])

        im = Image.open(io.BytesIO(post_data))
        im = im.resize((SIZE, SIZE))
        buf = io.BytesIO()
        im.save(buf, format='JPEG')
        buf.seek(0)

        t = time.time_ns() - t
        tt = time.thread_time_ns() - tt

        body = base64.b64encode(buf.read())

        res = {
            "statusCode": 200,
            "headers": {
                "Time": str(t),
                "Thread-Time": str(tt),
                "Server-UUID": SERVERID,
                "Content-Type": "image/jpeg",
            },
            "body": body.decode("UTF-8")
        }
    except Exception as e:
        res = {
                "statusCode": 200,
                "body":str(e),
        }
    return res
