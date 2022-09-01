from DB_conn.db import engine, meta
from models.user import user

meta.create_all(engine)
