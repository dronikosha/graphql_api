from DB_conn.db import meta
from sqlalchemy import Column, Integer, String, Table
from sqlalchemy.sql.sqltypes import Integer, String

user = Table('user', meta,
             Column('id', Integer, primary_key=True, autoincrement=True),
             Column('name', String(50)),
             Column('email', String(100)),
             Column('password', String(255))
             )
