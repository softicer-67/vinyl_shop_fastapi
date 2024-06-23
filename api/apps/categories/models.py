from sqlalchemy.orm import mapped_column, Mapped
from config.settings import Base


class Categories(Base):
    __tablename__='categories'

    id:Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    slug: Mapped[str] = mapped_column(unique=True)

    def __str__(self) -> str:
        return self.name