
from sqlalchemy import Table, MetaData, Column, Integer, VARCHAR, Text, ForeignKey, DateTime, Boolean, DECIMAL,INT

from sqlalchemy.dialects.postgresql import VARCHAR,INTEGER,  FLOAT
from sqlalchemy.schema import CreateColumn
from sqlalchemy.ext.compiler import compiles
from sqlalchemy import Table, Column, MetaData, Integer, Identity

def get_productb(metadata):

    product = Table('product', metadata,
    Column('id', INT, Identity (start=1, cycle=True), primary_key=True, nullable=False, unique=True, index = True, autoincrement=True),
    Column('title', VARCHAR(32), nullable=False, default=''),
    Column('ean', VARCHAR(32), nullable=False, default='',index = True),
    Column('price', DECIMAL(14,4), nullable=False, default=''),
    )
    return product


































