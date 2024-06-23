from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from ..base_repo.base_class import BaseService
from .models import Categories
from config.settings import get_session


class CategoriesService(BaseService[Categories]):

    def __init__(self, db_session: Session):
        super(CategoriesService, self).__init__(Categories, db_session)


def get_category_service(db_session: AsyncSession = Depends(get_session)) -> CategoriesService:
    return CategoriesService(db_session)