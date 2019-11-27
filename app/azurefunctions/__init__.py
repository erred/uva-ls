from PIL import Image
import azure.functions as func
import io
import os
import time
import uuid

SIZE = int(os.getenv("SIZE", "256"))
SERVERID = str(uuid.uuid4())

def main(req: func.HttpRequest) -> func.HttpResponse:
    t = time.time_ns()
    tt = time.thread_time_ns()

    post_data = req.get_body()
    im = Image.open(io.BytesIO(post_data))
    im = im.resize((SIZE, SIZE))
    buf = io.BytesIO()
    im.save(buf, format='JPEG')
    buf.seek(0)

    t = time.time_ns() - t
    tt = time.thread_time_ns() - tt

    return func.HTTPRespnse(
        body-buf.read(),
        status_code=200,
        headers={
            "Time": str(t),
            "Thread-Time": str(tt),
            "Server-UUID": SERVERID,
            "Content-Type": "image/jpeg"
        }
    )
