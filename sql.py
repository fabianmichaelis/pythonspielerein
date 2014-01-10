from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey

engine = create_engine('mysql+mysqldb://root:top@127.0.0.1/test')

metadata = MetaData()
links = Table('Links', metadata,
Column('id', Integer, primary_key=True),
Column('name', String(150)),
)

metadata.create_all(engine) 