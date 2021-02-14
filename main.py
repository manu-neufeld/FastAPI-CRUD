import uvicorn
from fastapi import FastAPI
from fastapi import APIRouter
import os
from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi_sqlalchemy import db
from post.model import Post as ModelPost
from post.schema import Post as SchemaPost
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

app = FastAPI()
app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])

@app.post("/post/", response_model=SchemaPost)
def create_post(post: SchemaPost):
    db_post = ModelPost(
        title=post.title, body=post.body, is_published=post.is_published, created=post.created, modified=post.modified
    )
    db.session.add(db_post)
    db.session.commit()
    return db_post

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)

