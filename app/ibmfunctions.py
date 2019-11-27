from PIL import Image
import base64
import io
import os
import time
import uuid

SIZE = int(os.getenv("SIZE", "256"))
# PORT = int(os.getenv("PORT", "8080"))
SERVERID = uuid.uuid4()

def main(args):
    try:
        t = time.time_ns()
        tt = time.thread_time_ns()

        post_data = event["body"]
        if event["isBase64Encoded"]:
            post_data = base64.decodebytes(post_data)

        im = Image.open(io.BytesIO(post_data))
        im = im.resize((SIZE, SIZE))
        buf = io.BytesIO()
        im.save(buf, format='jpg')
        buf.seek(0)

        t = time.time_ns() - t
        tt = time.thread_time_ns() - tt

        res = {
            "statusCode": 200,
            "headers": {
                "Time": str(t),
                "Thread-Time": str(tt),
                "Server-UUID": SERVERID,
                "Content-Type": "image/jpg",
            },
            "body": base64.encodebytes(buf.read())
        }
        print(res.headers)
    except Exception as e:
        print(str(e))
        res = {
            "statusCode": 500,
            "body":str(e)
        }
    return res
