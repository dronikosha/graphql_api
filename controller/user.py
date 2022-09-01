from DB_conn.db import conn
from fastapi import APIRouter
from models.user import user
from strawberry.asgi import GraphQL
from type.user import schema

user = APIRouter()
graphql = GraphQL(schema=schema)

user.add_route('/graphql', graphql)
