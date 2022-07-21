'''
To enjoy the advantages of asynchronous programing, it's necessary that
the methods, functions, classes, et cetera, used on the algorithm are 
structured in a way that allows this sort of programing.
In the code below, the package aiofile is shown.

Code related to the course "Programação Concorrente e Assíncrona com Python". 
Available at https://www.udemy.com/course/programacao-concorrente-e-assincrona-com-python/
'''
import asyncio
import aiofiles


async def example_1_text_file():
    async with aiofiles.open('./python_studies/async_concur/05_async/files/text.txt') as obj: #root = ESTUDOS_PYTHON
        content = await obj.read()
    print(content)

async def example_2_text_file():
    async with aiofiles.open('./python_studies/async_concur/05_async/files/text.txt') as obj:
        async for row in obj:
            print(row)

def main():
    el = asyncio.get_event_loop()
    el.run_until_complete(example_1_text_file())
    el.run_until_complete(example_2_text_file())
    el.close()
if __name__ == '__main__':
    main()


