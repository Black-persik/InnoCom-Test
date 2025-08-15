import sqlalchemy
from sqlalchemy import MetaData, Table

from models.users import users_table

metadata = MetaData()
snippets_table = Table(
    "snippets",
    metadata,
    sqlalchemy.Column("user_id", sqlalchemy.ForeignKey(users_table.c.user_id)),
    sqlalchemy.Column("snippet_id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("language", sqlalchemy.String(40)),
    sqlalchemy.Column("snippet_text", sqlalchemy.String(100_000))
)