from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase, declared_attr


class Base(DeclarativeBase):

    engine = create_async_engine('sqlite+aiosqlite:///db.sqlite3')
    session = async_sessionmaker(bind=engine)

    @declared_attr
    def __tablename__(cls):
        return ''.join(f'_{i.lower()}' if i.isupper() else i for i in cls.__name__).strip('_')

    @staticmethod
    def create_session(func):
        async def wrapper(*args, **kwargs):
            async with Base.session() as session:
                return await func(*args, **kwargs, session=session)

        return wrapper

    @create_session
    async def save(self, session: AsyncSession = None) -> None:
        session.add(self)
        await session.commit()
        await session.refresh(self)

    @classmethod
    @create_session
    async def get(cls, pk, session: AsyncSession = None):
        return await session.get(cls, pk)

    @create_session
    async def delete(self, session: AsyncSession = None):
        await session.delete(self)
        await session.commit()

    @classmethod
    @create_session
    async def select(cls, sql, session: AsyncSession = None):
        objs = await session.scalars(sql)
        return objs.all()
