import asyncio
import numpy as np
import pandas as pd

from aiohttp import ClientSession
from aiohttp import TCPConnector

from extract import *
from transform import *
from util import async_timed

#start_time = datetime.now().strftime('%d_%m_%Y_%H_%M_%S')
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
        df_aliquota_transformed = aliquotas_rpps_transform(df_aliquota)
        
        df_control = verify_uploaded_data(df_DIPR,df_aliquota)

        df_comparation = rpps_aliquota_vs_dipr(df_DIPR,df_aliquota_transformed)

        df_aliquota_transformed.to_excel('./downloaded_data/aliquotas_transformadas.xlsx')
        df_control.to_excel('./downloaded_data/df_controle.xlsx')
        df_comparation.to_excel('./downloaded_data/df_comparacao.xlsx')
        print("FIM DO PROCESSAMENTO")
    

asyncio.run(main())

