import asyncio
import numpy as np
import pandas as pd

from aiohttp import ClientSession
from aiohttp import TCPConnector
from datetime import datetime

from fetch import *
from util import async_timed

start_time = datetime.now().strftime('%d_%m_%Y_%H_%M_%S')
#logging.basicConfig(filename=f'./log/{start_time}.log', 
#                    level=logging.DEBUG)
@async_timed()       
async def main():
    async with ClientSession(connector=TCPConnector(
                            limit=64,
                            verify_ssl=False),
                            headers={'Accept':'application/json'}
                            ) as session:
        endpoint_cnpjs = EndpointRegPrev()
        cnpj_iter:np.ndarray = await endpoint_cnpjs.get_cnpjs(session)
        df_DIPR:pd.DataFrame = await EndpointBase.get_data(cnpj_iter,session,
                                                EndpointDIPR)
        df_aliquota:pd.DataFrame = await EndpointBase.get_data(cnpj_iter,session,
                                                EndpointRppsAliquota)
        print(len(df_DIPR))
        print(len(df_aliquota))
        #df_DIPR.to_excel('./downloaded_data/DIPR_ajuricaba.xlsx')
        df_aliquota.to_excel('./downloaded_data/ALIQUOTAS.xlsx')

asyncio.run(main())

