import asyncio
import aiohttp
import time
import glob, csv, datetime, os, json

q = asyncio.Queue(510)

urls = {'nevesserver0':'http://145.100.104.117:8080',
        'nevesserver1':'http://145.100.104.117:8080',
        'nevesserver2':'http://145.100.104.117:8080'}

def get_images():
    with open('./images', 'rb') as f:
        img = f.read()
        return [img * 10], [ [img * 50 ] * 50 ]



async def do_10(imgs, url):
    results = []
    async with aiohttp.ClientSession() as sess:
        for img in imgs:
            t = time.time_ns()
            r = await sess.post(url, data=img)
            t = time.time_ns() - t
            if r.status != 200:
                # log error
                continue
            results.append({
                'Date': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'Client_time' : t,
                'Server_time' : r.headers['Time'],
                'ServerThread_time' : r.headers['Thread-Time'],
                'Server-UUID' : r.headers['Server-UUID']
            })

    await q.put(results)



async def main():
    # imgss [[img * 10] * 50]
    img10, img500 = get_images()



    exit()
    for name, url in urls.items():
        t0 = time.time_ns()

        await do_10(img10, url)

        t1 = time.time_ns()

        aws = []
        for imgs in img500:
            aws.append(do_10(imgs, url))
        await asyncio.gather(*aws)

        t2 = time.time_ns()

        print(t1-t0, t2-t1)

if __name__ == "__main__":
    asyncio.run(main())
