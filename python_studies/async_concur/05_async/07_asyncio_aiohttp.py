'''
To enjoy the advantages of asynchronous programing, it's necessary that
the methods, functions, classes, et cetera, used on the algorithm are 
structured in a way that allows this sort of programing.
In the code below, the package aiohttp is shown.

Code related to the course "Programação Concorrente e Assíncrona com Python". 
Available at https://www.udemy.com/course/programacao-concorrente-e-assincrona-com-python/
'''
import asyncio
import aiofiles
import aiohttp
import bs4

async def get_links()->list:
    '''
    Asynchronous function to generate a list of urls.
    '''
    links = []
    async with aiofiles.open('./python_studies/async_concur/05_async/files/links.txt') as obj:
        async for link in obj:
            links.append(link.strip())
    return links

async def download_html(link:str)->str:
    '''
    Asynchronous function to download the html.
    '''
    print(f'link = {link}')
    async with aiohttp.ClientSession() as session:
        async with session.get(link) as resp:
            resp.raise_for_status() # if webpage status is less than 400, then raise an exception.
            return await resp.text()

def webpage_title(html:str)->list:
    '''
    Non-asynchronous function to scrap the webpage title.
    '''
    soup = bs4.BeautifulSoup(html,'html.parser')
    title = soup.select_one('title')
    if not title==None:
        title = title.text.split('|')[0].strip()
        return title

async def print_titles():
    '''
    Asynchronous function to print the webpage title.
    '''
    links = await get_links()
    tasks = [asyncio.create_task(download_html(link)) for link in links]
    for task in tasks:
        html = await task # while one task is been executed, other task are also been executed.
        title = webpage_title(html)
        print(f'title{title}')

def main():
    el = asyncio.get_event_loop()
    el.run_until_complete(print_titles())
    el.close()

if __name__=='__main__':
    main()