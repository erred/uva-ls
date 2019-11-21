from PIL import Image

new_size = (256, 256)

def process(im: Image.Image) -> Image.Image:
    return im.resize(new_size)

if __name__ == "__main__":
    im = Image.open('./image.jpeg')
    im = process(im)
    im.save('./image-small.jpeg')
