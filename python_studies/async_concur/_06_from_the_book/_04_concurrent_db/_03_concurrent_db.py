'''
It's possible to create a connection pool to a PostgreSQL database, 
via the package 'asyncpg'.

The code below was created by Matthew Fowler in the book 'Python 
Concurrency with asyncio-Manning Publications (2022)'. 
'''

import asyncio
import asyncpg

from db_data_information.db_sensitive_information import *
from util import *

product_query = \
    """
    SELECT
        p.product_id,
        p.product_name,
        p.brand_id,
        s.sku_id,
        pc.product_color_name,
        ps.product_size_name
    FROM product as p
    JOIN sku as s ON s.product_id = p.product_id
    JOIN product_color as pc ON pc.product_color_id = s.product_color_id
    JOIN product_size as ps ON ps.product_size_id = s.product_size_id
    WHERE p.product_id = 100

    """
@async_timed()
async def query_product(pool):
    '''
    Coroutine that grab a connection from the pool and execute a query.
    '''
    async with pool.acquire() as connection:
        return await connection.fetchrow(product_query)

async def main():
    
    async with asyncpg.create_pool( host=server_, # opening a connection to the database
                                port=port_,
                                user=user_,
                                database='products',
                                password=password_,
                                min_size=6,
                                max_size=6) as pool:# Create a connection pool with six connections.
            await asyncio.gather(query_product(pool), query_product(pool)) # starting the event loop
if(__name__=='__main__'):
    asyncio.get_event_loop().run_until_complete(main())  

    