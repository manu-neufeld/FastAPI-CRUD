from app.db.db import db
from app.db.tables import posts

class Post:
    @classmethod
    async def get(cls, id):
        query = posts.select().where(posts.c.id == id)
        post = await db.fetch_one(query)
        return post

    @classmethod
    async def get_all(cls):
        query = posts.select()
        db_posts = await db.fetch_all(query)
        return db_posts

    @classmethod
    async def create(cls, **post):
        query = posts.insert().values(**post)
        post = await db.execute(query)
        return post
