#!/usr/bin/env python3

from PIL import Image
import glob, requests, time, csv, datetime, os, asyncio


image_list = []
services_url = {'nevesserver0':'http://145.100.104.117:8080',
 				'nevesserver1':'http://145.100.104.117:8080',
 				'nevesserver2':'http://145.100.104.117:8080'}



def get_images():
	try:	
		for filename in glob.glob('/sne/home/mbadiassimo/LS/images/*.*')[:50]: 
			im=open(filename, 'rb')
			im1= im.read()
			im.close()
			image_list.append(im1)

	except Exception as e:
		with open('./logs/imageproblems.log', 'a') as logfile:
			logfile.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ': ' + str(e) + '\n')
		exit()


def save_results(name, results):
	try:
		if not os.path.isfile('./results/recursive_' + name + '.csv'):
			f = open('./results/iterative_' + name + '.csv', 'w')
			writer = csv.DictWriter(f, fieldnames=['Date', 'Client_time', 'Server_time', 'ServerThread_time', 'Server-UUID'])
			writer.writeheader()
			f.close()	

		with open('./results/recursive_' + name + '.csv', 'a') as csvFile:
			writer = csv.DictWriter(csvFile, fieldnames=['Date', 'Client_time', 'Server_time', 'ServerThread_time', 'Server-UUID'])
			for result in results:
				writer.writerow(result)

	except Exception as e:
		with open('./logs/log_recursive_' + name + '.log', 'a') as logfile:
			logfile.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '(save results error): ' + str(e)  + 'results are: ' + str(results) + '\n')


#we need to have this func running 50 times in parallel
async def do_requests(name, url):
	
	results = []
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
				'ServerThread_time' : r.headers['Thread-Time'],
				'Server-UUID' : r.headers['Server-UUID']
			}
			results.append(data)
		else:
			with open('./logs/log_iterative_' + name + '.log', 'a') as logfile:
				logfile.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ': Status code ' + str(r.status_code) + ', ERROR: ' +  str(r.reason))


async def main(name, url):
	aws = []
	for i in range(50):
		aws.append(do_requests())
	await asyncio.gather(*aws)


if __name__ == "__main__":
	get_images()

	for name, url in services_url.items():

		asyncio.run(main(name, url))
		pass
		#set de asyinc stuff
