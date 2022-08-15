import asyncio
import logging
import pandas as pd
import numpy

from aiohttp import ClientSession
from datetime import datetime
from typing import ClassVar
from pydantic import BaseModel

from .fetch_functions import fetch_result

# suppress FutureWarning
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

class EndpointBase(BaseModel):
    '''
    Base class related to the endpoint classes.
    '''
    sg_uf:str = 'RS'
    offset:int = 0
    df_created:ClassVar[bool] = False # true, if df was created; false, otherwise.
    
    @staticmethod
    async def get_data(cnpjs_list:numpy.ndarray,
                       session:ClientSession,
                       endpoint_class)->pd.DataFrame:
        '''
        Concept
        -------------------------
        This coroutine can request data from the endpoints of CADPREV API
        for various cnpjs and returns a Pandas DataFrame. 

        Parameters
        -------------------------
            cnpjs_list: a list of RPPS cnpjs
            session: an asynchronous session
        '''
        fn = lambda cnpj: asyncio.create_task(fetch_result(
                    session,endpoint_class(nr_cnpj_entidade = cnpj)))
        
        pending = list(map(fn,cnpjs_list))
        
        while pending: # while pending task, continue.
            done, pending = await asyncio.wait(
                            pending,return_when=asyncio.FIRST_COMPLETED)
            for done_task in done:
                print(f'Done task count: {len(done)}')
                print(f'Pending task count: {len(pending)}')
                if done_task.exception() is None:
                    if not endpoint_class.df_created: # if 'df' is empty, then it's the 1st round.
                        df = pd.DataFrame(done_task.result().data)
                        endpoint_class.df_created = True # df was created.
                    else:
                        df = df.append(pd.DataFrame(done_task.result().data))
                        '''
                        df= pd.concat([df,pd.DataFrame(
                                done_task.result().data)],ignore_index=True)
                        '''
                    if(done_task.result().row_limit_exc): # if row limit exceeded, then create a new task
                        done_task.result().inner_control.offset+=1
                        pending.add(asyncio.create_task(fetch_result(
                                session,done_task.result().inner_control))) #create a new task
                    print(len(df))
                                            
                else: # if an exception occurs, all pending_tasks will be cancelled.
                    logging.error("Request got an exception",
                                exc_info=done_task.exception())
                    for pending_task in pending: # if an error occurs, then cancel the remaining tasks.
                        pending_task.cancel()
                        pending = False
                    raise done_task.exception()
        return df

class EndpointDIPR(EndpointBase):
    '''
    Class related to the endpoint DIPR.
    '''
    nr_cnpj_entidade:str
    dt_ano:int = datetime.now().year -1
    endpoint:ClassVar[str] = 'DIPR'


class EndpointRppsAliquota(EndpointBase):
    '''
    Class related to the endpoint RPPS_ALIQUOTA.
    '''
    nr_cnpj_entidade:str
    endpoint:ClassVar[str] = 'RPPS_ALIQUOTA'


class EndpointRegPrev(EndpointBase):
    '''
    Class related to the endpoint RPPS_REGIME_PREVIDENCIARIO.
    '''
    tp_regime: str = 'RPPS'
    endpoint: ClassVar[str] = 'RPPS_REGIME_PREVIDENCIARIO'
    row_lim_exceeded:ClassVar[str] = True
    #nr_cnpj_entidade:str = '87613253000119'

    async def get_cnpjs(self,session:ClientSession)->numpy.ndarray:
        '''
        Concept
        -------------------------
        Coroutine that returns an iterator with cnpjs values where
        tp_vinculo_legislacao equals 'Criação do Regime' and
        dt_fim is null.

        Parameters
        ----------------------
            session:ClientSession
        
        '''
        while self.row_lim_exceeded: # iterate if row limit is true
            result = await  fetch_result(session=session,
                                        obj=self)
            EndpointRegPrev.row_lim_exceeded = result.row_limit_exc
            if result.row_limit_exc: # row limit exceeded, update offset 
                    self.offset+=1
            if not self.df_created:
                df_cnpjs = pd.DataFrame(result.data)
                EndpointRegPrev.df_created = True # if df_created, then not first iteration 
            else:
                df_cnpjs = df_cnpjs.append(pd.DataFrame(result.data))
            
        df_cnpjs = df_cnpjs.loc[ # filter tp_vinculo_legislacao equals 'Criação do Regime'
            df_cnpjs.tp_vinculo_legislacao == 'Criação do Regime'
            ]
        df_cnpjs = df_cnpjs[df_cnpjs.dt_fim.isna()] # only 'df_fim' null values
        df_cnpjs = df_cnpjs.nr_cnpj_entidade.unique() # only unique values for cnpj
        return df_cnpjs

