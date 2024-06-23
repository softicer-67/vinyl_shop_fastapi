from typing import Optional, List
# from typing_extensions import Annotated
from fastapi import APIRouter, Depends
from .service import ProductsService, get_product_service
from . import schema


app = APIRouter(prefix='/api/v1/products', tags=['Товары'])

@app.get(
        '/',
        summary='Список',
        response_model=List[schema.ProductInfo]
        )
async def list(
    limit: int,
    service: ProductsService = Depends(get_product_service)
    ):
    return await service.get_list(limit)

@app.get(
        '/{id}',
        summary='Один элемент',
        response_model=schema.ProductInfo
        )
async def get_one(
    id: int,
    service: ProductsService = Depends(get_product_service)
    ):
    return await service.get_one(id)

@app.post('/', summary='Создание', status_code=201)
async def create(
    data: schema.ProductCreateUpdate = Depends(),
    service: ProductsService = Depends(get_product_service)
    ):
    return await service.create(data)

@app.delete('/{id}', summary='Удаление')
async def delete(
    id: int,
    service: ProductsService = Depends(get_product_service)
    ):
    return await service.delete(id)