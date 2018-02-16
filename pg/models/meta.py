import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import MetaData
from sqlalchemy.ext.declarative import declarative_base

from ..config import get_config


NAMING_CONVENTION = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}


def get_engine():
    config = get_config()
    engine = sa.create_engine(get_config().database.conn_str,  echo=True)
    return engine


def get_base(engine):
    metadata = MetaData(naming_convention=NAMING_CONVENTION)
    Base = declarative_base(bind=engine, metadata=metadata)
    return Base


engine = get_engine()
Base = get_base(engine)
Session = sessionmaker(bind=engine)



__all__ = [
    "engine",
    "Base",
    "Session",
]
