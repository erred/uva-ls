from PIL import Image
import base64
import io
import os
import time
import traceback
import uuid

SIZE = int(os.getenv("SIZE", "256"))
SERVERID = str(uuid.uuid4())


# https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
def handler(event, context):
    t = time.time_ns()
    tt = time.thread_time_ns()

    post_data = base64.b64decode(event["body"])
    # post_data = event["body"]
    # if event["isBase64Encoded"]:
    #     post_data = base64.b64decode(post_data)

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
        "isBase64Encoded": True,
        "body": base64.b64encode(buf.read()),
    }
    return res
