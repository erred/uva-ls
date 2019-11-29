from PIL import Image
import http.server
import io
import os
import socketserver
import time
import uuid

SIZE = int(os.getenv("SIZE", "256"))
SERVERID = str(uuid.uuid4())

class handler(http.server.BaseHTTPRequestHandler):

    def do_POST(self):
        try:
            st0 = time.clock_gettime(time.CLOCK_REALTIME)
            tt0 = time.clock_gettime(time.CLOCK_THREAD_CPUTIME_ID)

            post_data = self.rfile.read(int(self.headers['Content-Length']))

            st1 = time.clock_gettime(time.CLOCK_REALTIME)
            tt1 = time.clock_gettime(time.CLOCK_THREAD_CPUTIME_ID)

            im = Image.open(io.BytesIO(post_data))
            im = im.resize((SIZE, SIZE))
            buf = io.BytesIO()
            im.save(buf, format='JPEG')

            st2 = time.clock_gettime(time.CLOCK_REALTIME)
            tt2 = time.clock_gettime(time.CLOCK_THREAD_CPUTIME_ID)

            buf.seek(0)
            buffed = buf.read()

            st3 = time.clock_gettime(time.CLOCK_REALTIME)
            tt3 = time.clock_gettime(time.CLOCK_THREAD_CPUTIME_ID)

            self.send_response(200)

            self.send_header("Time", ', '.join([str(int(1000000000 * x)) for x in [st1-st0, st2-st1, st3-st2]]))
            self.send_header("Thread-Time", ', '.join([str(int(1000000000 * x)) for x in [tt1-tt0, tt2-tt1, tt3-tt2]]))
            self.send_header("Server-UUID", SERVERID)
            self.send_header("Content-Type", "image/jpeg")
            self.end_headers()
            self.wfile.write(buffed)
        except Exception as e:
            self.send_error(500, message=str(e))
