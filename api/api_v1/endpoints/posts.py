from fastapi import APIRouter, Depends, HTTPException
from fastapi_sqlalchemy import db
from models.post import Post as ModelPost
from schemas.post import Post as SchemaPost
from typing import List

router = APIRouter()

@router.get("/post/", response_model=List[SchemaPost])
def get_all_post():
    db_posts = db.session.query(ModelPost).all()
    return db_posts

@router.get("/post/{id}", response_model=SchemaPost)
def get_post(id: int):
    db_post = db.session.query(ModelPost).get(id)
    return db_post

@router.post("/post/", response_model=SchemaPost)
def create_post(post: SchemaPost):
    db_post = ModelPost(
        title=post.title, body=post.body, is_published=post.is_published, created=post.created, modified=post.modified
    )
    db.session.add(db_post)
    db.session.commit()
    return db_post

@router.patch("/post/{id}", response_model=SchemaPost)
def modify_post(post: SchemaPost):
    db_post = ModelPost(
        id=post.id, title=post.title, body=post.body, is_published=post.is_published, created=post.created, modified=post.modified
    )
    db.session.merge(db_post)
    db.session.commit()
    return db_post

@router.delete("/post/{id}", response_model=SchemaPost)
def delete_post(id: int):
    db_post = db.session.query(ModelPost).get(id)
    db.session.delete(db_post)
    db.session.commit()
