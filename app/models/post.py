from typing import Optional
from pydantic import BaseModel, Field, validator
from datetime import datetime

from pydantic.errors import DataclassTypeError
from app.models.rwmodel import RWModel

class PostSchema(RWModel):
    title: str
    body: str 
    is_published : bool

class PostDB(RWModel):
    id: int
    title: str
    body: str 
    is_published : bool
    created : Optional[datetime]
    modified : Optional[datetime]

class PostKey(BaseModel):
    id: int
