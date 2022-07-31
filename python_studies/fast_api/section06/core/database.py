from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession

from core.configs import settings_

engine : AsyncEngine = create_async_engine(settings_.DB_URL) # creates an assynchronous engine

Session: AsyncSession = sessionmaker( # 'Session' is the constructor of a session.
    autocommit=False, # commits are manual
    autoflush=False, 
    expire_on_commit=False, # session stays open after a commit
    class_ = AsyncSession,
    bind=engine
)
