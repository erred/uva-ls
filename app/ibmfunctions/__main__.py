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
    t = time.time_ns()
    tt = time.thread_time_ns()

    post_data = args["body"]
    if event["isBase64Encoded"]:
        post_data = base64.decodebytes(post_data)

    im = Image.open(io.BytesIO(post_data))
    im = im.resize((SIZE, SIZE))
    buf = io.BytesIO()
    im.save(buf, format='JPEG')
    buf.seek(0)

    t = time.time_ns() - t
    tt = time.thread_time_ns() - tt

    res = {
        "statusCode": 200,
        "headers": {
            "Time": str(t),
            "Thread-Time": str(tt),
            "Server-UUID": SERVERID,
            "Content-Type": "image/jpeg",
        },
        "body": base64.encodebytes(buf.read())
    }
    return res
