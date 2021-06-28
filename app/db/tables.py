from sqlalchemy import (Column, DateTime, Integer, String, Boolean, Table)
from sqlalchemy.sql import func
from app.db.db import metadata

posts = Table(
    "posts",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String),
    Column("body", String),
    Column("is_published", Boolean),
    Column("created", DateTime, default=func.now(), nullable=False),
    Column("modified", DateTime, onupdate=func.now()),
)