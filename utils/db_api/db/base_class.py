from sqlalchemy import Integer
from sqlalchemy.ext.declarative import declared_attr, declarative_base
from sqlalchemy.orm import Mapped, mapped_column


class CustomBase:
    # Generate auto id and table name
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    @declared_attr
    def __table__(cls):
        return cls.__name__.lower()


Base = declarative_base(cls=CustomBase)
