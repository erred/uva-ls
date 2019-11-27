from PIL import Image
import io
import os
import datetime
import uuid

SIZE = int(os.getenv("SIZE", "256"))
SERVERID = uuid.uuid4()

def main(env, start_response):
    try:
        t = datetime.time()

        post_data = env["wsgi.input"].read(int(env.get('CONTENT_LENGTH', 0)))

        im = Image.open(io.BytesIO(post_data))
        im = im.resize((SIZE, SIZE))
        buf = io.BytesIO()
        im.save(buf, format='JPEG')
        buf.seek(0)

        td = datetime.now() - t

        start_response("200 OK", [
            ("Time", str(1000 * td / timedelta(microseconds=1))),
            ("Thread-Time", str(1000 * td / timedelta(microseconds=1))),
            ("Server-UUID", SERVERID),
            ("Content-Type", "image/jpeg"),
        ])
        return [buf.read()]

    except Exception as e:
        start_response("500 "+str(e), [])
        return []
