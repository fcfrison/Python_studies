from core.configs import settings_
from core.database import engine
import asyncio

import models

async def create_tables()->None:
    
    async with engine.begin() as conn:
        await conn.run_sync(settings_.DBBaseModel.metadata.drop_all)
        await conn.run_sync(settings_.DBBaseModel.metadata.create_all)
    print('Tables created.')

if (__name__=="__main__"):
    asyncio.get_event_loop().run_until_complete(create_tables())