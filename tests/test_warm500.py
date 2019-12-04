import glob, requests, time, csv
import datetime, os, asyncio, queue
import itertools, aiohttp

services_url = {'zeit-now-warm':'https://warm.lsproject.now.sh/api/zeit',
                'gcp-run-warm':'https://warm-6jdjoh342a-ew.a.run.app/',
                'gcp-fun-warm':'https://europe-west1-cedar-channel-259712.cloudfunctions.net/warm',
                'azure-fun-warm':'https://lsproject.azurewebsites.net/api/warm',
                'ibm-fun-warm':'https://eu-gb.functions.cloud.ibm.com/api/v1/web/marbadias97%40gmail.com_dev/default/warm',
                'ali-fun-warm':'https://5055975195697149.eu-central-1.fc.aliyuncs.com/2016-08-15/proxy/warm/warm/',
                'gcp-app-warm': 'https://warm-dot-cedar-channel-259712.appspot.com/',
                'aws-lambda-warm':'https://xt8gn4dt7g.execute-api.eu-west-2.amazonaws.com/default/warm'
            }

res = asyncio.Queue()
err = asyncio.Queue()


def divide_list(l, n):
    for i in range(0, len(l), n):  
        yield l[i:i + n] 


def get_images():
    try:
        image_list = []
        for filename in glob.glob('../../images/images_resized/*.*')[:500]:
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
        if not os.path.isfile('./results/warm/test500w_' + name + '.csv'):
            f = open('./results/warm/test500w_' + name + '.csv', 'w')
            writer = csv.DictWriter(f, fieldnames=['Date', 'Client_time', 'Server_time', 'ServerThread_time', 'Server-UUID', 'Worker', 'Img'])
            writer.writeheader()
            f.close()

        with open('./results/warm/test500w_' + name + '.csv', 'a') as csvFile:
            writer = csv.DictWriter(csvFile, fieldnames=['Date', 'Client_time', 'Server_time', 'ServerThread_time', 'Server-UUID', 'Worker', 'Img'])

            while not res.empty():
                x = await res.get()
                for i in x:
                    writer.writerow(i)

        #if there is any error save it in a log file
        while not err.empty():
            with open('./logs/test500w_' + name + '.log', 'a') as logfile:
                y = await err.get()
                logfile.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + y + '\n')

    except Exception as e:
        with open('./logs/test500w_' + name + '.log', 'a') as logfile:
            logfile.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '(save results error): ' + str(e) + '\n')



async def do_requests(url, imgs, count):
    try:
        results = []
        async with aiohttp.ClientSession() as sess:
            count2 = 0
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
                    'Server-UUID' : r.headers['Server-UUID'],
                    'Worker': str(count),
                    'Img': str(count2)
                })
                count2+=1
        await res.put(results)

    except Exception as e:
        await err.put(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ' ' + str(e) + '\n')

            
async def main():
    img500 = get_images()
    for name, url in services_url.items():
        aws = []
        count = 0
        for imgs in img500:
            aws.append(do_requests(url, imgs, count))
            count+=1
        await asyncio.gather(*aws)
        await save_results(name)

if __name__ == "__main__":
    asyncio.run(main())
    
