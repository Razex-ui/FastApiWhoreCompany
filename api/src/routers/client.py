from fastapi.routing import APIRouter
from pydantic import UUID4
from src.schemas.client import Client, ClientDB , ClientUpdate, ClientFilter
from src.models.client import ClientsSQL

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete, update

from src.db.session import get_session

from src.service.client import ClientService

router = APIRouter(prefix="/client", tags=['Client'])


@router.post("/create", tags=['Создание'])
async def create(body: Client, db_session: AsyncSession = Depends(get_session)) -> ClientDB:
    return await ClientService.create(body, db_session)

@router.post("/get_with_filter", tags=['Отфильтровать'])
async def get_filter(filter_by: ClientFilter, db_session: AsyncSession = Depends(get_session)) -> list[ClientDB]:
    return await ClientService.get_with_filter(filter_by, db_session)

@router.get("/get_all", tags=['Получить всё'])
async def get_all(db_session: AsyncSession = Depends(get_session)) -> list[ClientDB]:
    return await ClientService.get_all(db_session)


@router.get("/get${uid}", tags=['Получить одно'])
async def get_one(uid: UUID4, db_session: AsyncSession = Depends(get_session)) -> ClientDB:
    return await ClientService.get_one(uid, db_session)

@router.put("/update", tags=['Обновить одно'])
async def update_one(uid: UUID4, body: ClientUpdate, db_session: AsyncSession = Depends(get_session)) -> ClientDB:
    return await ClientService.update_one(uid, db_session)


@router.delete("/delete${uid}", tags=['Удалить один элемент'])
async def delete_one(uid: UUID4, db_session: AsyncSession = Depends(get_session)):
   return await ClientService.delete_one(uid, db_session)


@router.delete("/delete_all", tags=['Удалить всё'])
async def delete_all(db_session: AsyncSession = Depends(get_session)):
    return await ClientService.delete_all(db_session)
