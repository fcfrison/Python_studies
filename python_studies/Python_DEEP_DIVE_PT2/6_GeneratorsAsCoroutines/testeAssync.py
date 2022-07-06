import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(f"finished at {time.strftime('%X')}")
    print(what)

async def main():
    task1 = asyncio.create_task(
        say_after(5, 'hello'))

    task2 = asyncio.create_task(
        say_after(1, 'world'))
    
    task3 = asyncio.create_task(
        say_after(8, 'frison'))

    task4 = asyncio.create_task(
        say_after(7, 'felipe'))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2
    await task3
    await task4

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())
