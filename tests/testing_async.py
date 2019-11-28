#!/usr/bin/env python3

from PIL import Image
import glob, requests, time, csv, datetime, os, asyncio, queue


image_list = []
services_url = {'nevesserver0':'http://145.100.104.117:8080'}


res = queue.Queue()
err = queue.Queue()


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


def save_results(name):
	try:
		if not os.path.isfile('./results/recursive_' + name + '.csv'):
			f = open('./results/recursive_' + name + '.csv', 'w')
			writer = csv.DictWriter(f, fieldnames=['Date', 'Client_time', 'Server_time', 'ServerThread_time', 'Server-UUID'])
			writer.writeheader()
			f.close()	

		with open('./results/recursive_' + name + '.csv', 'a') as csvFile:
			writer = csv.DictWriter(csvFile, fieldnames=['Date', 'Client_time', 'Server_time', 'ServerThread_time', 'Server-UUID'])

			while not res.empty():
				x = res.get()
				for i in x:
					writer.writerow(i)

		#if there is any error save it in a log file
		while not err.empty():
			with open('./logs/log_recursive_' + name + '.log', 'a') as logfile:
				y = err.get()
				logfile.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + y + '\n')

	except Exception as e:
		with open('./logs/log_recursive_' + name + '.log', 'a') as logfile:
			logfile.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '(save results error): ' + str(e) + '\n')



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
			error = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ': Status code ' + str(r.status_code) + ', ERROR: ' +  str(r.reason)
			err.put(error)
	#store the results of the 10 requests in the queue
	res.put(results)


async def main(name, url):
	aws = []
	for i in range(50):
		aws.append(do_requests(name, url))
	await asyncio.gather(*aws)


if __name__ == "__main__":
	get_images()

	for name, url in services_url.items():
		asyncio.run(main(name, url))
		save_results(name)
