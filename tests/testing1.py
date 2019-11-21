#!/usr/bin/env python3

from PIL import Image
import glob, requests, time, csv, datetime, os

services_url = {'localhost0':'http://localhost:8080',
 				'localhost1':'http://localhost:8080',
 				'localhost2':'http://localhost:8080'}


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


#get 10 images
def get_images():
	image_list = []
	for filename in glob.glob('/sne/home/mbadiassimo/LS/images/*.*')[:10]: 
		im=open(filename, 'rb')
		im1= im.read()
		im.close()
		image_list.append(im1)
	return image_list



if __name__ == "__main__":
	image_list = get_images()
	print(len(image_list))

	for name, url in services_url.items():
		try:

			#prepare the file for writing the results
			#if file does not exists, create and write headers
			if not os.path.isfile('iterative_' + name + '.csv'):
				f = open('iterative_' + name + '.csv', 'w')
				writer = csv.DictWriter(f, fieldnames=['Date', 'Client_time', 'Server_time', 'ServerThread_time'])
				writer.writeheader()
				f.close()

			#we send the request, mesure time and save results 10 times
			for i in range(10):

				var = image_list[i]
				t = time.time_ns()
				r = requests.post(url, data=var)
				total_time = time.time_ns() - t
				if r.status_code == 200:
					data = {
						'Date': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 
						'Client_time' : total_time,
						'Server_time' : r.headers['Time'],
						'ServerThread_time' : r.headers['Thread-Time']
					}

					try:
						with open('iterative_' + name + '.csv', 'a') as csvFile:
							writer = csv.DictWriter(csvFile, fieldnames=['Date', 'Client_time', 'Server_time', 'ServerThread_time'])
							writer.writerow(data)

					except Exception as e:
						raise e
						#log file?


				else:
					#log services errors
					print(r.status_code)
					pass

		except Exception as e:
			print(str(e))
			#maybe do a log file



















