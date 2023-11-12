from contextlib import asynccontextmanager

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

from data.config import DATABASE_URL

engine = create_async_engine(DATABASE_URL)
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


@asynccontextmanager
async def get_session() -> AsyncSession:
    async with async_session() as session:
        try:
            yield session
            await session.commit()
        except SQLAlchemyError as sql_error:
            await session.rollback()
            raise sql_error
        finally:
            await session.close()
