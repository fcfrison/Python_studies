import asyncio
import logging
from aiohttp import ClientSession
from aiohttp import TCPConnector
from extract import fetch_status_w_delay
from util import async_timed


async def main():
    list_endpoints = ['DIPR']
    list_cnpj = [
        '92406495000171','87531976000179','92465228000175',
        '87612933000118','92406057000103','92123926000192',
        '88000906000157','92411156000183'
    ]
    list_cnpj =['92406495000171',]
    base_url = 'https://apicadprev.economia.gov.br/'
    novo_dict = {'cnpj':{'sg_uf':'RS','nr_cnpj_entidade':'01','offset':0,'dt_ano':2022}}
    db_cnpjs = dict()
    url_list = list()
    url_parameters = '?sg_uf=RS&nr_cnpj_entidade={cnpj}&offset={offset}&dt_ano=2022'
    for endpoint in list_endpoints:
        for cnpj in list_cnpj:
            db_cnpjs[cnpj] = 0
            url_list.append(base_url+endpoint+
                            url_parameters.format(cnpj=cnpj,offset=0))
    headers = { 'Accept': 'application/json'}
    async with ClientSession(connector=TCPConnector(limit=64,verify_ssl=False),
                            headers=headers) as session:

        pending = [asyncio.create_task(fetch_status_w_delay(session, url)) 
                    for url in url_list]
        while pending: # while pending task, continue.
            done, pending = await asyncio.wait(pending,
                                    return_when=asyncio.FIRST_COMPLETED)
            print(f'Done task count: {len(done)}')
            print(f'Pending task count: {len(pending)}')
            for done_task in done:
                if done_task.exception() is None:
                    print(print(done_task.result()))
                else:
                    logging.error("Request got an exception",
                                exc_info=done_task.exception())
                    for pending_task in pending: # if an error occurs, the cancel the remaining tasks.
                        pending_task.cancel()
                        pending = False
asyncio.run(main())


