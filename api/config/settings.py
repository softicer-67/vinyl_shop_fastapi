import os
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from dotenv import load_dotenv


load_dotenv('.env')

DB = os.getenv('POSTGRES_DB')
PASSWORD = os.getenv('POSTGRES_PASSWORD')
USER = os.getenv('POSTGRES_USER')

# строка подключения
bd_url = f'postgresql+asyncpg://{USER}:{PASSWORD}@data_base:5432/{DB}'

# создаем движок SqlAlchemy
engine = create_async_engine(bd_url, pool_pre_ping=True)

#создаем базовый класс для моделей
class Base(DeclarativeBase):
    pass


async def get_session():
    async_session = async_sessionmaker(engine, expire_on_commit=False)
    async with async_session() as session:
        yield session
        await session.close()
