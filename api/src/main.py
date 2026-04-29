import uvicorn
from fastapi import FastAPI
from fastapi.routing import APIRouter
from src.config import settings

from src.routers.whore import router as whore_router
from src.routers.pimp import router as pimp_router
from src.routers.client import router as client_router
from src.routers.client_whore import router as client_whore_router
from src.routers.characteristics_whore import router as characteristic_whore_router
from src.routers.characteristics import router as characteristic_router

tags_metadata = [
    {
        "name": 'Создание',
        "description": 'Создать одну запись'
    },
    {
        "name": 'Отфильтровать',
        "description": 'Отфильтровать по характеристикам'
    },
    {
        "name": 'Получить всё',
        "description": 'Вывести всё'
    },
    {
        "name": 'Получить одно',
        "description": 'Вывести одно'
    },
    {
        "name": 'Обновить одно',
        "description": 'Обновить по UID'
    },
    {
        "name": 'Удалить один элемент',
        "description": 'Удаление одного элемента'
    },
    {
        "name": 'Удалить всё',
        "description": 'Удаление всех элементов'
    }
]

app = FastAPI(
    openapi_url=f"{settings.BASE_ROUTE_PATH}/openapi.json",
    docs_url=f"{settings.BASE_ROUTE_PATH}/docs",
    openapi_tags=tags_metadata
)

@app.get('/api/v1/version')
def get_version():
    return 1

router = APIRouter(prefix=settings.BASE_ROUTE_PATH)

router.include_router(whore_router, prefix="/whore", tags=['Whore'])
router.include_router(pimp_router, prefix="/pimp", tags=['Pimp'])
router.include_router(client_router, prefix="/client", tags=['Client'])
router.include_router(client_whore_router, prefix="/client_whore", tags=['Client_whore'])
router.include_router(characteristic_whore_router, prefix="/characteristics_whore", tags=['Characteristics_whore'])
router.include_router(characteristic_router, prefix="/characteristics", tags=['Characteristics'])

app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='localhost',
        port=8500,
        reload=True,
    )

# ДЗ посмотреть гит на ютубе
