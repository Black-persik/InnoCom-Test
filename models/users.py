import sqlalchemy
from sqlalchemy import Table, MetaData
from sqlalchemy.dialects.postgresql import UUID
metadata = MetaData()

users_table = Table(
    "users",
    metadata,
    sqlalchemy.Column("user_id", UUID(as_uuid=False), server_default=sqlalchemy.text("uuid_generate_v4()"), nullable=False, unique=True, index=True),
    sqlalchemy.Column("email", sqlalchemy.String(100), unique=True, nullable=False),
    sqlalchemy.Column("username", sqlalchemy.String(40), nullable=False)
)


