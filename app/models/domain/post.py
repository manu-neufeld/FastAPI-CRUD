from app.models.common import DateTimeModelMixin, IDModelMixin
from app.models.domain.rwmodel import RWModel


class Post(IDModelMixin, DateTimeModelMixin, RWModel):
    title: str
    body: str
    is_published: bool
