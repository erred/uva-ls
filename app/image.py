from PIL import Image
import http.server
import io
import os
import socketserver
import time
import uuid

SIZE = int(os.getenv("SIZE", "256"))
PORT = int(os.getenv("PORT", "8080"))
SERVERID = uuid.uuid4()

class Handler(http.server.BaseHTTPRequestHandler):

    def do_POST(self):
        try:
            t = time.time_ns()
            tt = time.thread_time_ns()

            post_data = self.rfile.read(int(self.headers['Content-Length']))
            im = Image.open(io.BytesIO(post_data))
            im = im.resize((SIZE, SIZE))
            buf = io.BytesIO()
            im.save(buf, format='jpeg')
            buf.seek(0)

            t = time.time_ns() - t
            tt = time.thread_time_ns() - tt

            1 /0

            self.send_response(200)
            self.send_header("Time", str(t))
            self.send_header("Thread-Time", str(tt))
            self.send_header("Server-UUID", SERVERID)
            self.end_headers()
            self.wfile.write(buf.read())
        except Exception as e:
            self.rror_message_format = "%"
            self.send_error(500, message=str(e))

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()
