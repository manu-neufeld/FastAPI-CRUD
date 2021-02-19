from app.db.db import db
from app.models.post import PostSchema
from app.db.tables import posts

async def get_all():
    query = posts.select()
    return await db.fetch_all(query=query)

async def create(payload: PostSchema):
    query = posts.insert().values(**payload.dict())
    return await db.execute(query=query)

async def get(id: int):
    query = posts.select().where(id == posts.c.id)
    return await db.fetch_one(query=query)

async def put(id: int, payload: PostSchema):
    query = (
        posts
        .update()
        .where(id == posts.c.id)
        .values(**payload.dict())
        .returning(posts.c.id)
    )
    return await db.execute(query=query)

async def delete(id: int):
    query = posts.delete().where(id == posts.c.id)
    return await db.execute(query=query)