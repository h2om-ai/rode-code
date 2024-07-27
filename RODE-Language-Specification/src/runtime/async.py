import time
import asyncio

async def sleep(duration):
    await asyncio.sleep(duration / 1000)

async def async_function():
    print("Start async function")
    await sleep(1000)
    print("End async function")

# Example usage
if __name__ == '__main__':
    asyncio.run(async_function())
