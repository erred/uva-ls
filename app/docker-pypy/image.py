from PIL import Image
import http.server
import io
import os
import socketserver
from datetime import datetime, timedelta
import uuid

SIZE = int(os.getenv("SIZE", "256"))
PORT = int(os.getenv("PORT", "8080"))
SERVERID = str(uuid.uuid4())

class Handler(http.server.BaseHTTPRequestHandler):

    def do_POST(self):
        t = datetime.now()

        post_data = self.rfile.read(int(self.headers['Content-Length']))
        im = Image.open(io.BytesIO(post_data))
        im = im.resize((SIZE, SIZE))
        buf = io.BytesIO()
        im.save(buf, format='JPEG')
        buf.seek(0)

        td = datetime.now() - t

        self.send_response(200)
        self.send_header("Time", str(1000 * td / timedelta(microseconds=1)))
        self.send_header("Thread-Time", str(1000 * td / timedelta(microseconds=1)))
        self.send_header("Server-UUID", SERVERID)
        self.send_header("Content-Type", "image/jpeg")
        self.end_headers()
        self.wfile.write(buf.read())

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()
