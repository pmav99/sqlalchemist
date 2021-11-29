import sqlalchemy as sa

from .meta import Base


class Person(Base):
    __tablename__ = "person"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String)
    date_of_birth = sa.Column(sa.Date)
    height = sa.Column(sa.Integer)
    weight = sa.Column(sa.Numeric)


__all__ = [
    "Person",
]
