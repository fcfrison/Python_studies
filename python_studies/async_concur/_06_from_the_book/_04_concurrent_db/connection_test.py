import asyncpg
import asyncio

from db_data_information.db_sensitive_information import *

async def main():
    connection = await asyncpg.connect( host=server_,
                                        port=port_,
                                        user=user_,
                                        database=server_name_,
                                        password=password_)
    version = connection.get_server_version()
    print(f'Connected! Postgres version is {version}')
    await connection.close()
asyncio.run(main())