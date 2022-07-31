import asyncio
import pandas as pd
import logging
from aiohttp import ClientSession
from aiohttp import TCPConnector
from fetch import fetch_status_altered
from util import async_timed


async def main():
    list_endpoints = ['DIPR']
    list_cnpj =['92406495000171','87531976000179']
    db_cnpjs = dict()
    state = None
    for endpoint in list_endpoints:
        for cnpj in list_cnpj:
            db_cnpjs[cnpj] = {
                'sg_uf':'RS','nr_cnpj_entidade':cnpj,
                'offset':0,'dt_ano':2022,'endpoint':endpoint
                }

    async with ClientSession(connector=TCPConnector(
                            limit=64,verify_ssl=False),
                            headers={'Accept':'application/json'}
                            ) as session:

        pending = [asyncio.create_task(fetch_status_altered(
                    session, db_cnpjs[key])) for key in db_cnpjs]
        while pending: # while pending task, continue.
            done, pending = await asyncio.wait(
                            pending,return_when=asyncio.FIRST_COMPLETED)

            print(f'Done task count: {len(done)}')
            print(f'Pending task count: {len(pending)}')
            for done_task in done:
                if done_task.exception() is None:
                    if not state: # if 'df' is empty, then it's the 1st round.
                        df = pd.DataFrame(done_task.result()
                             [0]['results'][0]['data'])
                        state = True
                    else:
                        df = df.append(pd.DataFrame(
                                done_task.result()[0]['results']
                                [0]['data']))
                    print(len(df))
                else: # if an exception occurs, all pending_tasks will be cancelled.
                    logging.error("Request got an exception",
                                exc_info=done_task.exception())
                    for pending_task in pending: # if an error occurs, the cancel the remaining tasks.
                        pending_task.cancel()
                        pending = False
asyncio.run(main())
