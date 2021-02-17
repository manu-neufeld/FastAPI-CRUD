from fastapi import APIRouter, Depends, HTTPException, Path
from fastapi_sqlalchemy import db
import app.services.post as ServicePost
from app.models.post import PostKey, PostSchema, PostDB 
from typing import List

router = APIRouter()

@router.post("/post/", response_model=PostKey, status_code=201)
async def create_post(payload: PostSchema):
    post_id = await ServicePost.create(payload)
    response_object = {
        "id": post_id
    }    
    return response_object

@router.get("/post/", response_model=List[PostDB])
async def get_all_post():
    posts = await ServicePost.get_all()
    return posts

@router.get("/post/{id}/", response_model=PostDB)
async def get_post(id: int = Path(..., gt=0),):
    post = await ServicePost.get(id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@router.put("/post/{id}/", response_model=PostKey)
async def modify_post(payload: PostSchema, id: int = Path(..., gt=0),):
    post = await ServicePost.get(id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    post_id = await ServicePost.put(id, payload)
    response_object = {
        "id": post_id
    }    
    return response_object    
    
@router.delete("/post/{id}/", response_model=None)
async def delete_post(id: int = Path(..., gt=0)):
    post = await ServicePost.get(id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    await ServicePost.delete(id)
