from PIL import Image
import base64
import io
import os
import time
import traceback
import uuid

SIZE = int(os.getenv("SIZE", "256"))
# PORT = int(os.getenv("PORT", "8080"))
SERVERID = uuid.uuid4()

def handler(event, context):
    t = time.time_ns()
    tt = time.thread_time_ns()

    post_data = base64.b64decode(event["body"])

    im = Image.open(io.BytesIO(post_data))
    im = im.resize((SIZE, SIZE))
    buf = io.BytesIO()
    im.save(buf, format='jpg')
    buf.seek(0)

    t = time.time_ns() - t
    tt = time.thread_time_ns() - tt

    res = {
        "statusCode": 200,
        "statusDescription": "200 OK",
        "headers": {
            "Time": str(t),
            "Thread-Time": str(tt),
            "Server-UUID": SERVERID,
            "Content-Type": "image/jpg",
        },
        "isBase64Encoded": True,
        "body": base64.b64encode(buf.read())
    }
    return res
