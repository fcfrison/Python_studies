# Exemplo 1 de asyncio - a execução vai até o final de main() e 
# depois executa a 'task'.
import asyncio
async def main():
    print('felipe')
    task = asyncio.create_task(foo('frison'))
    print('fim')

async def foo(text):
    print(text)
    await asyncio.sleep(1)

asyncio.run(main())


# Exemplo 2 de asyncio - a execução aguarda por task e 
# depois executa segue na função.
async def main():
    print('felipe')
    task = asyncio.create_task(foo('frison'))
    await task
    print('fim')

async def foo(text):
    print(text)
    await asyncio.sleep(1)

asyncio.run(main())
