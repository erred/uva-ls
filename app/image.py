from PIL import Image
import http.server
import socketserver
import os
import io
import time

SIZE = int(os.getenv("SIZE", "256"))
PORT = int(os.getenv("PORT", "8080"))

class Handler(http.server.BaseHTTPRequestHandler):

    def do_POST(self):
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

        self.send_response(200)
        self.send_header("Time", str(t))
        self.send_header("Thread-Time", str(tt))
        self.end_headers()
        self.wfile.write(buf.read())

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()
