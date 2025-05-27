from typing import Optional, List

from pydantic import BaseModel, Field

from constants.roles import Roles


class User(BaseModel):
    email: str = Field(..., pattern=r".*@.*")
    fullName: str
    password: str = Field(..., min_length=8)
    passwordRepeat: str
    roles: List[Roles]
    banned: Optional[bool] = None
    verified: Optional[bool] = None

