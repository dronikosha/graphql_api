import typing
from data_cipher import Encoder
import strawberry
from DB_conn.db import conn
from models.index import user
from config import key


encoder = Encoder()


@strawberry.type
class User:
    id: int
    name: str
    email: str
    passwrod: str


@strawberry.type
class Query:
    @strawberry.field
    def user(self, id: int) -> User:
        return conn.execute(user.select().where(user.c.id == id)).fetchone()

    @strawberry.field
    def users(self) -> typing.List[User]:
        return conn.execute(user.select()).fetchall()

    @strawberry.field
    def user_by_email(self, email: str) -> User:
        return conn.execute(user.select().where(user.c.email == email)).fetchone()

    @strawberry.field
    def user_by_name(self, name: str) -> User:
        return conn.execute(user.select().where(user.c.name == name)).fetchone()

    @strawberry.field
    def user_by_email_name(self, email: str, name: str) -> User:
        return conn.execute(user.select().where(user.c.email == email and user.c.name == name)).fetchone()


@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_user(self, name: str, email: str, password: str) -> str:
        conn.execute(user.insert().values(
            name=name, email=email, password=str(encoder.aes_encrypt(password, key))))
        return "success"

    @strawberry.mutation
    def update_user(self, id: int, name: str, email: str, password: str) -> str:
        conn.execute(user.update().where(user.c.id == id).values(
            name=name, email=email, password=str(encoder.aes_encrypt(password, key))))
        return "success"

    @strawberry.field
    def delete_user(self, id: int) -> str:
        conn.execute(user.delete().where(user.c.id == id))
        return "success"

    @strawberry.field
    def delete_users(self) -> str:
        conn.execute(user.delete())
        return "success"

    @strawberry.field
    def delete_user_by_email(self, email: str) -> str:
        conn.execute(user.delete().where(user.c.email == email))
        return "success"

    @strawberry.field
    def delete_user_by_name(self, name: str) -> str:
        conn.execute(user.delete().where(user.c.name == name))
        return "success"


schema = strawberry.Schema(query=Query, mutation=Mutation)
