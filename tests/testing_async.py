#!/usr/bin/env python3

import glob, requests, time, csv
import datetime, os, asyncio, queue
import itertools, aiohttp

services_url = {'nevesserver0':'http://145.100.104.117:8080'}


res = asyncio.Queue()
err = asyncio.Queue()


def divide_list(l, n):
    for i in range(0, len(l), n):  
        yield l[i:i + n] 


def get_images():
    try:
        image_list = []
        for filename in glob.glob('../images/*.*')[:500]:
            im=open(filename, 'rb')
            im1= im.read()
            im.close()
            image_list.append(im1)
        return [x for x in divide_list(image_list, 10)]

    except Exception as e:
        with open('./logs/imageproblems.log', 'a') as logfile:
           logfile.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ': ' + str(e) + '\n')
        exit()


async def save_results(name):
    try:
        if not os.path.isfile('./results/recursive_' + name + '.csv'):
            f = open('./results/recursive_' + name + '.csv', 'w')
            writer = csv.DictWriter(f, fieldnames=['Date', 'Client_time', 'Server_time', 'ServerThread_time', 'Server-UUID'])
            writer.writeheader()
            f.close()

        with open('./results/recursive_' + name + '.csv', 'a') as csvFile:
            writer = csv.DictWriter(csvFile, fieldnames=['Date', 'Client_time', 'Server_time', 'ServerThread_time', 'Server-UUID'])

            while not res.empty():
                x = await res.get()
                for i in x:
                    writer.writerow(i)

        #if there is any error save it in a log file
        while not err.empty():
            with open('./logs/log_recursive_' + name + '.log', 'a') as logfile:
                y = await err.get()
                logfile.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + y + '\n')

    except Exception as e:
        with open('./logs/log_recursive_' + name + '.log', 'a') as logfile:
            logfile.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '(save results error): ' + str(e) + '\n')



async def do_requests(url, imgs):
    try:
        results = []
        async with aiohttp.ClientSession() as sess:
            for img in imgs:
                t = time.time_ns()
                r = await sess.post(url, data=img)
                total_time = time.time_ns() - t
                if r.status != 200:
                    await err.put(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ': Status code ' + str(r.status_code) + ', ERROR: ' +  str(r.reason) +'\n')
                    continue 

                results.append({
                    'Date': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'Client_time' : total_time,
                    'Server_time' : r.headers['Time'],
                    'ServerThread_time' : r.headers['Thread-Time'],
                    'Server-UUID' : r.headers['Server-UUID']
                })
        await res.put(results)

    except Exception as e:
        print('this error')
        await err.put(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ' ' + str(e) + '\n')

            

async def main():
    img500 = get_images()

    for name, url in services_url.items():
        aws = []
        for imgs in img500:
            aws.append(do_requests(url, imgs))
        await asyncio.gather(*aws)
        await save_results(name)

if __name__ == "__main__":
    asyncio.run(main(), debug=True)
    
