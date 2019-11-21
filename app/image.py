from PIL import Image
import http.server
import socketserver

NEW_SIZE = (256, 256)
PORT = 8080

class Handler(http.server.BaseHTTPRequestHandler):

    def do_POST(self):

    def process(im: Image.Image) -> Image.Image:
        return im.resize(new_size)


def serve():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()


if __name__ == "__main__":
    im = Image.open('./image.jpeg')
    im = process(im)
    im.save('./image-small.jpeg')
