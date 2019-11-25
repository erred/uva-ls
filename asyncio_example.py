import asyncio
import aiohttp
import time
import glob, csv, datetime, os, json

q = asyncio.Queue(50)
urls = {'nevesserver0':'http://145.100.104.117:8080',
        'nevesserver1':'http://145.100.104.117:8080',
        'nevesserver2':'http://145.100.104.117:8080'}

def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

def get_images():
    try:    
        image_list = []
        for filename in glob.glob('/sne/home/mbadiassimo/LS/images/*.*')[:5]: 
            im=open(filename, 'rb')
            im1= im.read()
            im.close()
            image_list.append(im1)

        return list(chunks(image_list, 10))

    except Exception as e:
        with open('./logs/imageproblems.log', 'a') as logfile:
            logfile.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ': ' + str(e) + '\n')
        exit()


async def do_10(imgs, url):
    results = []
    for img in imgs:
        t = time.time_ns()
        r = await aiohttp.post(url, data=img)
        t = time.time_ns() - t
        if resp.status != 200:
            # log error
            continue
        results.append({
            'Date': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 
            'Client_time' : t,
            'Server_time' : r.headers['Time'],
            'ServerThread_time' : r.headers['Thread-Time'],
            'Server-UUID' : r.headers['Server-UUID']
        })
        
    q.put(results)



async def main():
    # imgss [[img * 10] * 50]
    imgss = get_images()
    for name, url in urls:
        for imgs in imgss:
            aws.append(do_10(imgs, url))
        await asyncio.gather(*aws)


        # read results from q

if __name__ == "__main__":
    asyncio.run(main())
