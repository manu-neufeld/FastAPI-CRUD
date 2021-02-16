from app.db.db import metadata
import sqlalchemy

posts = sqlalchemy.Table(
    "posts",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("title", sqlalchemy.String),
    sqlalchemy.Column("body", sqlalchemy.String),
    sqlalchemy.Column("is_published", sqlalchemy.Boolean),
    sqlalchemy.Column("created", sqlalchemy.DateTime),
    sqlalchemy.Column("modified", sqlalchemy.DateTime),
)