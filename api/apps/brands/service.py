from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from ..base_repo.base_class import BaseService
from .models import Brands
from config.settings import get_session


class BrandService(BaseService[Brands]):

    def __init__(self, db_session: Session):
        super(BrandService, self).__init__(Brands, db_session)


def get_brand_service(db_session: AsyncSession = Depends(get_session))-> BrandService:
    return BrandService(db_session)
