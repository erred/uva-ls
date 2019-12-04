#2048x2048

from PIL import Image
import glob

def get_images():
    try:
        image_list = []
        for filename in glob.glob('../images/*.*'): 
            name = filename.split('/')[-1]
            im = Image.open(filename)
            im = im.resize((2048,2048))
            im.save('/sne/home/mbadiassimo/LS/images/images_resized/'+ name, format='JPEG')

    except Exception as e:
        print(str(e))


get_images()