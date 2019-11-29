from PIL import Image
import http.server
import io
import os
import socketserver
import time
import uuid

SIZE = int(os.getenv("SIZE", "256"))
PORT = int(os.getenv("PORT", "8080"))
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
            self.send_header("Clock-Res", time.clock_getres(time.CLOCK_REALTIME) + ", ", time.clock_getres(time.CLOCK_THREAD_CPUTIME_ID))
            self.send_header("Time", ', '.join(map(str, [int(1000000000 * st1-st0), int(1000000000 * st2-st1), int(1000000000 * st3-st2)])))
            self.send_header("Thread-Time", ', '.join(map(str, [int(1000000000 * tt1-tt0), int(1000000000 * tt2-tt1), int(1000000000 * tt3-tt2)])))
            self.send_header("Server-UUID", SERVERID)
            self.send_header("Content-Type", "image/jpeg")
            self.end_headers()
            self.wfile.write(buffed)
        except Exception as e:
            self.send_error(500, message=str(e))

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()
