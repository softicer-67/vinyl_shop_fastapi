from typing import Optional
from pydantic import BaseModel


class BrandCreateUpdate(BaseModel):
    id: Optional[int] = None
    name: str
    slug: str

    class Config:
        orm_mode = True


class BrandInfo(BrandCreateUpdate):
    id: int