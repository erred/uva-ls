#2048x2048

from PIL import Image
import glob

def get_images():
    try:
        image_list = []
        count = 0
        for filename in glob.glob('../images/raw/*.*'): 
            name = filename.split('/')[-1]
            print(count, name)
            im = Image.open(filename)
            im = im.resize((2048,2048))
            im.save('../images/images_resized/'+ name, format='JPEG')
            count+=1
    except Exception as e:
        print(str(e))


get_images()
