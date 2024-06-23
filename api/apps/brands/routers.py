from typing import List

from fastapi import APIRouter, Depends
from .service import BrandService, get_brand_service
from . import schema


app = APIRouter(prefix='/api/v1/brands', tags=['Бренды'])


@app.get(
        '/',
        summary='Список',
        response_model=List[schema.BrandInfo]
        )
async def list(
    limit: int,
    service: BrandService = Depends(get_brand_service)
    ):
    return await service.get_list(limit)

@app.get(
        '/{id}',
        summary='Один элемент',
        response_model=schema.BrandInfo
        )
async def get_one(
    id: int,
    service: BrandService = Depends(get_brand_service)
    ):
    return await service.get_one(id)

@app.post('/', summary='Создание', status_code=201)
async def create(
    data: schema.BrandCreateUpdate,
    service: BrandService = Depends(get_brand_service)
    ):
    return await service.create(data)

@app.delete('/{id}', summary='Удаление')
async def delete(
    id: int,
    service: BrandService = Depends(get_brand_service)
    ):
    return await service.delete(id)