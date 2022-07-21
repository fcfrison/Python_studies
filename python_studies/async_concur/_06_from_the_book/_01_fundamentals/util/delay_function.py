import asyncio


async def delay(delay_seconds: int) -> int:
    '''
    Coroutine to delay the execution of the code.
    '''
    print(f'sleeping for {delay_seconds} second(s)')
    await asyncio.sleep(delay_seconds)
    print(f'finished sleeping for {delay_seconds} second(s)')
    return delay_seconds