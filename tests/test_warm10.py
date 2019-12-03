#!/usr/bin/env python3

import glob, requests, time, csv, datetime, os, json

services_url = {'zeit-now-warm':'https://warm.lsproject.now.sh/api/zeit',
				'cp-run-warm':'https://warm-6jdjoh342a-ew.a.run.app/',
				'gcp-fun-warm':'https://europe-west1-cedar-channel-259712.cloudfunctions.net/warm',
				'azure-fun-warm':'https://lsproject.azurewebsites.net/api/warm',
				'ibm-fun-warm':'https://eu-gb.functions.cloud.ibm.com/api/v1/web/marbadias97%40gmail.com_dev/default/warm',
				'ali-fun-warm':'https://5055975195697149.eu-central-1.fc.aliyuncs.com/2016-08-15/proxy/warm/warm/'
			}



#get 10 images
def get_images():
	try:
		image_list = []
		for filename in glob.glob('../../images/*.*')[:10]: 
			im=open(filename, 'rb')
			im1= im.read()
			im.close()
			image_list.append(im1)
		return image_list

	except Exception as e:
		with open('./logs/imageproblems.log', 'a') as logfile:
			logfile.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ': ' + str(e) + '\n')
		exit()

	

#prepare the file for writing the results
#if file does not exists, create and write headers
def save_results(name, results):
	try:
		if not os.path.isfile('./results/warm/test10w_' + name + '.csv'):
			f = open('./results/warm/test10w_' + name + '.csv', 'w')
			writer = csv.DictWriter(f, fieldnames=['Date', 'Client_time', 'Server_time', 'ServerThread_time', 'Server-UUID'])
			writer.writeheader()
			f.close()	

		with open('./results/warm/test10w' + name + '.csv', 'a') as csvFile:
			writer = csv.DictWriter(csvFile, fieldnames=['Date', 'Client_time', 'Server_time', 'ServerThread_time', 'Server-UUID'])
			for result in results:
				writer.writerow(result)

	except Exception as e:
		with open('./logs/test10w_' + name + '.log', 'a') as logfile:
			logfile.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '(save results error): ' + str(e)  + 'results are: ' + str(results) + '\n')




if __name__ == "__main__":
	image_list = get_images()
	for name, url in services_url.items():
		try:
			#we send the request, mesure time and save results 10 times
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
					with open('./logs/test10w_' + name + '.log', 'a') as logfile:
						logfile.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ': Status code ' + str(r.status_code) + ', ERROR: ' +  str(r.reason) +'\n')
			
			save_results(name, results)

		except Exception as e:
			with open('./logs/test10w_' + name + '.log', 'a') as logfile:
				logfile.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ': ' + str(e) + '\n')



















