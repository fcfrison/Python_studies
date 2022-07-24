'''
When we are dealing with databases, errors can happen. A way to handle with it
is through commits and rollbacks. If an error occurs, 'asyncpg' will automatically
rollback. The code presented here deals with these concepts.

The code below was created by Matthew Fowler in the book 'Python 
Concurrency with asyncio-Manning Publications (2022)'. 
'''
import asyncio
import logging
import asyncpg

from db_data_information.db_sensitive_information import *

async def main():
    connection = await asyncpg.connect( host=server_, # opening a connection to the database
                                        port=port_,
                                        user=user_,
                                        database='products',
                                        password=password_)
    try:
        async with connection.transaction(): # instead of dealing directly with a connection
                                             # a better approach is to deal with a transaction.
                                             # If an error occured, then everything will be rolled back.
            insert_brand = "INSERT INTO brand VALUES(9999, 'big_brand')"
            await connection.execute(insert_brand) # executing a statement
            await connection.execute(insert_brand)
    except Exception:
        logging.exception('Error while running transaction')
    finally:
        query = """SELECT brand_name FROM brand WHERE brand_name LIKE 'big_%'"""
        brands = await connection.fetch(query)
        print(f'Query result was: {brands}')
        await connection.close()

if(__name__=='__main__'):
    asyncio.get_event_loop().run_until_complete(main()) 