'''
Creating tables via SQLAlchemy on a PostgreSQL database.
'''

import asyncio
from core.configs import settings_
from core.database import engine # the engine already has been configured given
                                 # a specific configuration (user, password, ...)
async def create_tables():
    async with engine.begin() as connection: # opening a connection
        #await connection.run_sync(settings_.DBBaseModel.metadata.drop_all) # drop all existing table
        await connection.run_sync(settings_.DBBaseModel.metadata.create_all) # the models that inherit from
                                                                             # DBBaseModel are those will be created 
                                                                             # on the database.
        print("Tables created.")
if (__name__=='__main__'):
    asyncio.get_event_loop().run_until_complete(create_tables())  