from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from config.settings import Base, engine


# Создаем экземпляр FastAPI
app = FastAPI()

# Монтируем статические файлы
app.mount('/static', StaticFiles(directory='static'), name='static')


# Настройка CORS
origin_cors = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origin_cors,
    allow_methods=['*'],
    allow_headers=['*']
)

@app.on_event('startup')
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


# Добавляем подприложения FastAPI
from apps.categories.routers import app as category_app
from apps.brands.routers import app as brand_app
from apps.products.routers import app as product_app

app.include_router(category_app)
app.include_router(brand_app)
app.include_router(product_app)



