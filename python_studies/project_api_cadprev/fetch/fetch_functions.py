from aiohttp import ClientSession
from collections import namedtuple
from typing import Union

from util import async_timed

#from .fetch_classes import EndpointDIPR,EndpointRegPrev

@async_timed() 
async def fetch_result(session: ClientSession, obj):
    '''
        Coroutine that take in a session and an object and return 
        the data from an specific endpoint. 

        parameters
        --------------------
        session: ClientSession
        url: str
        delay: int 
    '''
    async with session.get(f'https://apicadprev.economia.gov.br/{obj.endpoint}',
                            params=obj.dict()) as result:
        ApiReturn = namedtuple( 'ApiReturn','result_set data row_count '+ 
                                'row_limit_exc inner_control')
        returned_json = await result.json()
        returned_results,*_ = returned_json['results']
        api_return = ApiReturn(
            returned_results['resultSet'],
            returned_results['data'], 
            returned_results['rowCount'],
            returned_results['rowLimitExceeded'],
            obj)
        return api_return