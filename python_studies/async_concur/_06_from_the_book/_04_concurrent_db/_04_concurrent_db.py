'''
It's possible to create a connection pool to a PostgreSQL database, 
via the package 'asyncpg'. In the code presented here, 10000 queries
are executed via a connection pool with 6 connections.

The code below was created by Matthew Fowler in the book 'Python 
Concurrency with asyncio-Manning Publications (2022)'. 
'''
import asyncio
import asyncpg
from util import async_timed
from db_data_information.db_sensitive_information import *

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
        JOIN sku as s on s.product_id = p.product_id
        JOIN product_color as pc on pc.product_color_id = s.product_color_id
        JOIN product_size as ps on ps.product_size_id = s.product_size_id
        WHERE p.product_id = 100
        """
@async_timed()
async def query_product(pool):
    '''
    Coroutine that grabs a connection from the connection pool and execute a query.
    '''
    async with pool.acquire() as connection:
        return await connection.fetchrow(product_query)

@async_timed()
async def query_products_concurrently(pool:asyncpg.Pool, queries:int):
    '''
    Coroutine that starts the execution of the event loop.
    '''
    queries = [query_product(pool) for _ in range(queries)] # Generates coroutine objects.
    return await asyncio.gather(*queries)


async def main():
    
    async with asyncpg.create_pool( host=server_, # opening a connection to the database
                                port=port_,
                                user=user_,
                                database='products',
                                password=password_,
                                min_size=12,
                                max_size=12) as pool:# Create a connection pool with 12 connections.
        await query_products_concurrently(pool,10000)
if(__name__=='__main__'):
    asyncio.get_event_loop().run_until_complete(main())  
