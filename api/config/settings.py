from pydantic_settings import BaseSettings
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase


class Settings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_DB: str
    POSTGRES_PASSWORD: str


info = Settings()

# строка подключения
bd_url = f'postgresql+asyncpg://{info.POSTGRES_USER}:{info.POSTGRES_PASSWORD}@localhost:5432/{info.POSTGRES_DB}'

# создаем движок SqlAlchemy
engine = create_async_engine(bd_url)  # , pool_pre_ping=True)


# создаем базовый класс для моделей
class Base(DeclarativeBase):
    pass


async def get_session():
    async_session = async_sessionmaker(engine, expire_on_commit=False)
    async with async_session() as session:
        yield session
        await session.close()
