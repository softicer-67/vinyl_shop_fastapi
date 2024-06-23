from sqlalchemy import ForeignKey, ForeignKeyConstraint
from apps.brands.models import Brands
from apps.categories.models import Categories
from sqlalchemy.orm import mapped_column, Mapped, relationship
from config.settings import Base


class Products(Base):
    __tablename__='products'

    id:Mapped[int] = mapped_column(primary_key=True)
    group_name: Mapped[str]
    album_name: Mapped[str]
    album_year: Mapped[str]
    body_list: Mapped[str]
    price: Mapped[float]
    image: Mapped[str]

    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
    brand_id: Mapped[int] = mapped_column(ForeignKey("brands.id"))

    category: Mapped['Categories'] = relationship(Categories, lazy='joined')
    brand: Mapped['Brands'] = relationship(Brands, lazy='joined')

    def __str__(self) -> str:
        return self.name