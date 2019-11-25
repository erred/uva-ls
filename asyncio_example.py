import asyncio
import aiohttp
import time

q = asyncio.Queue(50)
urls = ["..."]

async def do_10(imgs, url):
    results = []
    for img in imgs:
        t = time.time_ns()
        resp = await aiohttp.post(url, data=img)
        t = time.time_ns() - t
        if resp.status != 200:
            # log error
            continue
        results.append({
            # fill results
        })
    q.put(results)



async def main():
    # imgss [[img * 10] * 50]

    for url in urls:
        for imgs in imgss:
            aws.append(do_10(imgs, url))
        await asyncio.gather(*aws)
        # read results from q

if __name__ == "__main__":
    asyncio.run(main())
