from sqlalchemy import MetaData, Table, Column, Integer, String

metadata = MetaData()

todos = Table(
    'todos',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('task', String(100), nullable=False,)
)