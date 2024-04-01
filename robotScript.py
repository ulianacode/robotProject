
import asyncio
import sys

async def count_n(start_number: int = 0):
    while True:
        print(start_number)
        start_number += 1
        await asyncio.sleep(1)

if __name__ == "__main__":
    start_number = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    asyncio.run(count_n(start_number))
