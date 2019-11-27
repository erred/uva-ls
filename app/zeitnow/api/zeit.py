from PIL import Image
import http.server
import io
import os
import socketserver
# import time
from datetime import datetime
from datetime import timedelta
import uuid

SIZE = int(os.getenv("SIZE", "256"))
SERVERID = str(uuid.uuid4())

class handler(http.server.BaseHTTPRequestHandler):

    def do_POST(self):
        # t = time.time_ns()
        # tt = time.thread_time_ns()
        t = datetime.now()

        post_data = self.rfile.read(int(self.headers['Content-Length']))
        im = Image.open(io.BytesIO(post_data))
        im = im.resize((SIZE, SIZE))
        buf = io.BytesIO()
        im.save(buf, format='JPEG')
        buf.seek(0)

        # t = time.time_ns() - t
        # tt = time.thread_time_ns() - tt
        t = datetime.now() - t

        self.send_response(200)
        self.send_header("Time", str(1000 * t / timedelta(microseconds=1)))
        self.send_header("Thread-Time", str(1000 * t / timedelta(microseconds=1)))
        self.send_header("Server-UUID", SERVERID)
        self.send_header("Content-Type", "image/jpeg")
        self.end_headers()
        self.wfile.write(buf.read())
