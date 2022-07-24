'''
The code presented here shows how to create tables in a PostgreSQL
database, via asyncpg. Before execute it, it's necessary to create 
a database called 'products'.

The code below was created by Matthew Fowler in the book 'Python 
Concurrency with asyncio-Manning Publications (2022)'. 
'''

import asyncpg
import asyncio

from db_data_information.db_sensitive_information import *
from sql_statements import *


async def main():
    
    connection = await asyncpg.connect( host=server_, # opening a connection to the database
                                        port=port_,
                                        user=user_,
                                        database='products',
                                        password=password_)
    version = connection.get_server_version() 
    print(f'Connected! Postgres version is {version}')
    
    statements = [CREATE_BRAND_TABLE,
                CREATE_PRODUCT_TABLE,
                CREATE_PRODUCT_COLOR_TABLE,
                CREATE_PRODUCT_SIZE_TABLE,
                CREATE_SKU_TABLE,
                SIZE_INSERT,
                COLOR_INSERT]
    print('Creating the product database...')
    
    for statement in statements: # looping over an iterator.
        status = await connection.execute(statement) # executing queries
        print(status)
        print('Finished creating the product database!')
    await connection.close()

asyncio.run(main())