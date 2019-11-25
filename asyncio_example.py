import asyncio
import time

async def s():
    # time.sleep(5)
    await asyncio.sleep(5)

async def main():
    aws = []
    for i in range(5):
        aws.append(s())
    await asyncio.gather(*aws)

if __name__ == "__main__":
    asyncio.run(main())
