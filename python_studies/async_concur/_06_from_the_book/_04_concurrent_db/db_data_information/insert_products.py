import asyncio
import asyncpg
from random import randint, sample
from typing import List, Tuple
from insert_brands import load_common_words
from db_sensitive_information import *

def gen_products(common_words: List[str],
                brand_id_start: int,
                brand_id_end: int,
                products_to_create: int) -> List[Tuple[str, int]]:
    '''
    Function that procudes a list of products and its ids.
    '''

    products = []
    for _ in range(products_to_create):
        description = [common_words[index] for index in sample(range(1000), 10)] # pick 10 words
        brand_id = randint(brand_id_start, brand_id_end)
        products.append((" ".join(description), brand_id))
    return products

def gen_skus(product_id_start: int,
            product_id_end: int,
            skus_to_create: int) -> List[Tuple[int, int, int]]:
    '''
    Function that generates a list of items.
    '''
    skus = []
    for _ in range(skus_to_create):
        product_id = randint(product_id_start, product_id_end)
        size_id = randint(1, 3)
        color_id = randint(1, 2)
        skus.append((product_id, size_id, color_id))
    return skus

async def main():
    common_words = load_common_words() # Loading the list of common words.
    connection = await asyncpg.connect( host=server_, # opening a connection to the database
                                        port=port_,
                                        user=user_,
                                        database='products',
                                        password=password_)

    product_tuples = gen_products(  common_words,
                                    brand_id_start=1,
                                    brand_id_end=100,
                                    products_to_create=1000)
    await connection.executemany("INSERT INTO product VALUES(DEFAULT, $1, $2)",
                                product_tuples)
    sku_tuples = gen_skus(product_id_start=1,
                            product_id_end=1000,
                            skus_to_create=100000)
    await connection.executemany("INSERT INTO sku VALUES(DEFAULT, $1, $2, $3)",
                                sku_tuples)
    await connection.close()
    
if __name__=="__main__":
    asyncio.run(main())
