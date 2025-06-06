import datetime
from typing import Dict

from pydantic import BaseModel, Field

from enums.locations import Locations


class CreatedMovieResponse(BaseModel):
    id: int
    name: str
    price: int
    description: str
    imageUrl: str = Field(pattern=r"^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?(\?\S*)?(#\S*)?$")
    location: Locations
    published: bool
    genreId: int = Field(ge=1, le=10)
    genre: Dict[str, str]
    createdAt: datetime.datetime
    rating: int = Field(ge=0, le=5)
