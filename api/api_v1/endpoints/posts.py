from fastapi import APIRouter, Depends, HTTPException
from fastapi_sqlalchemy import db
from models.post import Post as ModelPost
from schemas.post import Post as SchemaPost

router = APIRouter()

@router.post("/post/", response_model=SchemaPost)
def create_post(post: SchemaPost):
    db_post = ModelPost(
        title=post.title, body=post.body, is_published=post.is_published, created=post.created, modified=post.modified
    )
    db.session.add(db_post)
    db.session.commit()
    return db_post