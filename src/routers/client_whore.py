from fastapi.routing import APIRouter
from pydantic import UUID4

from src.schemas.client_whore import ClientWhore, ClientWhoreDB, ClientWhoreUpdate
from src.models.client_whore import ClientsWhoreSQL

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete, update

from src.db.session import get_session

from src.service.client_whore import ClientWhoreService

router = APIRouter(prefix="/client_whore", tags=['Client_whore'])


@router.post("/create", tags=['Создание'])
async def create(body: ClientWhore, db_session: AsyncSession = Depends(get_session)) -> ClientWhoreDB:
    return await ClientWhoreService.create(body, db_session)    


@router.get("/get_all", tags=['Получить всё'])
async def get_all(db_session: AsyncSession = Depends(get_session)) -> list[ClientWhoreDB]:
    return await ClientWhoreService.get_all(db_session)

@router.get("/get${uid}", tags=['Получить одно'])
async def get_one(uid: UUID4, db_session: AsyncSession = Depends(get_session)) -> ClientWhoreDB:
    return await ClientWhoreService.create(uid, db_session)

@router.put("/update", tags=['Обновить одно'])
async def update_one(uid: UUID4, body: ClientWhoreUpdate, db_session: AsyncSession = Depends(get_session)) -> ClientWhoreDB:
    return await ClientWhoreService.update_one(uid, body, db_session)


@router.delete("/delete${uid}", tags=['Удалить один элемент'])
async def delete_one(uid: UUID4, db_session: AsyncSession = Depends(get_session)):
    return await ClientWhoreService.delete_one(uid, db_session)


@router.delete("/delete_all", tags=['Удалить всё'])
async def delete_all(db_session: AsyncSession = Depends(get_session)):
    return await ClientWhoreService.delete_all(db_session)
