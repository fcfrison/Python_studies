'''
The code presented here insert random name of brands in a PostgreSQL
database using the package 'asyncpg' to do so.

The code below was created by Matthew Fowler in the book 'Python 
Concurrency with asyncio-Manning Publications (2022)'. 
'''

import asyncpg
import asyncio
from typing import List, Tuple
from random import sample
from db_sensitive_information import *

def load_common_words() -> List[str]:
    '''
    Function that reads the file 'common_words' and returns a list.
    '''
    with open('python_studies\\async_concur\_06_from_the_book\_04_concurrent_db\db_data_information\common_words.txt') as common_words:
        return common_words.readlines()

def generate_brand_names(words: List[str]) -> List[Tuple[str]]:
    '''
    Function that returns a random list of words.
    '''
    return [(words[index],) for index in sample(range(100), 100)]


async def insert_brands(common_words, connection) -> int:
    '''
    Coroutine the insert registers into the table 'brand'.
    '''
    brands = generate_brand_names(common_words)
    insert_brands = "INSERT INTO brand VALUES(DEFAULT, $1)"
    return await connection.executemany(insert_brands, brands)

async def main():
    common_words = load_common_words() # load words
    connection = await asyncpg.connect( host=server_, # opening a connection to the database
                                        port=port_,
                                        user=user_,
                                        database='products',
                                        password=password_)
                                        
    await insert_brands(common_words, connection)

if __name__=="__main__":
    asyncio.run(main())