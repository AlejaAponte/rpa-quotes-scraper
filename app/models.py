from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

# Tabla intermedia muchos-a-muchos
quote_tag_table = Table(
    'quote_tag',
    Base.metadata,
    Column('quote_id', Integer, ForeignKey('quotes.id')),
    Column('tag_id', Integer, ForeignKey('tags.id'))
)

class Quote(Base):
    __tablename__ = 'quotes'

    id = Column(Integer, primary_key=True)
    text = Column(String, unique=True, nullable=False)
    author = Column(String, nullable=False)

    tags = relationship('Tag', secondary=quote_tag_table, back_populates='quotes')

class Tag(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    quotes = relationship('Quote', secondary=quote_tag_table, back_populates='tags')
