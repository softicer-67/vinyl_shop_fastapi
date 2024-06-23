from fastapi import UploadFile, File, Form
from dataclasses import dataclass
from pydantic import BaseModel
from apps.categories.schema import CategoryInfo
from apps.brands.schema import BrandInfo


@dataclass
class ProductCreateUpdate:
    group_name: str = Form(...)
    album_name: str = Form(...)
    album_year: str = Form(...)
    body_list: str = Form(...)
    price: float = Form(...)
    image: UploadFile = File(...)
    category_id: int = Form(...)
    brand_id: int = Form(...)

class ProductInfo(BaseModel):
    id: int
    group_name: str
    album_name: str
    album_year: str
    body_list: str
    price: float
    image: str
    category: CategoryInfo
    brand: BrandInfo

    class Config:
        orm_mode = True
