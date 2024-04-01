import asyncio

async def printNumbers(startNum: int = 0):
    while True:
        print(startNum)
        startNum = startNum + 1
        await asyncio.sleep(1)


if __name__ == "__main__":
    startNum = 0
    asyncio.run(printNumbers(startNum))
