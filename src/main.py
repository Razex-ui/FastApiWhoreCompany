import uvicorn
from fastapi import FastAPI
from fastapi.routing import APIRouter
from src.config import settings

from routers.whore import router as whore_router
# from routers.default import router as default_router


app = FastAPI(
    openapi_url=f"{settings.BASE_ROUTE_PATH}/openapi.json",
    docs_url=f"{settings.BASE_ROUTE_PATH}/docs",
)

router = APIRouter(prefix=settings.BASE_ROUTE_PATH)

router.include_router(whore_router)
# router.include_router(default_router)

app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='localhost',
        port=8500,
        reload=True,
    )
