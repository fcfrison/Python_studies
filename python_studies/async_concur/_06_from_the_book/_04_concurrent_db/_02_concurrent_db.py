import asyncpg
import asyncio
from asyncpg import Record
from typing import List

from db_data_information.db_sensitive_information import *
from sql_statements import *


async def main():
    
    connection = await asyncpg.connect( host=server_, # opening a connection to the database
                                        port=port_,
                                        user=user_,
                                        database='products',
                                        password=password_)
    await connection.execute("INSERT INTO brand"+\
                            " VALUES(DEFAULT, 'Levis')")  # notice that 'connection' being a coroutine, the 
    await connection.execute("INSERT INTO brand VALUES(DEFAULT, 'Seven')") # way to call it is through an await statement.
    
    brand_query = 'SELECT brand_id, brand_name FROM brand'
    results: List[Record] = await connection.fetch(brand_query)
    for brand in results:
        print(f'id: {brand["brand_id"]}, name: {brand["brand_name"]}')
    await connection.close()

asyncio.get_event_loop().run_until_complete(main()) 