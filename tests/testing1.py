#!/usr/bin/env python3

from PIL import Image
import glob, requests

#TODO
''' get image and resize it to de desired size
	send it to the services we are testing and compute how long does it take to answer
	get the answer, take the time in the headesr, claculate what u need.
	save the data.

	We need:
	Repeate 10 times:
	- sending one request. Wait answer.

	Repeate 50 times in paralel
	- sending 10 request without wainting answer. '''

def get_images():
	image_list = []
	for filename in glob.glob('./images/*.jpg'): 
		im=Image.open(filename)
		image_list.append(im)
	return image_list


if __name__ == "__main__":
	image_list = get_images()
	r = requests.get('http://github.com/')
	print(r.status_code)




















