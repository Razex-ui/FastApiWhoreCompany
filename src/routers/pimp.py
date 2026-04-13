from fastapi.routing import APIRouter
from pydantic import UUID4
from src.schemas.pimp import Pimp, PimpDB, PimpUpdate
from src.models.pimp import PimpsSQL

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete, update

from src.db.session import get_session

from src.service.pimp import PimpService

router = APIRouter(prefix="/pimp", tags=['Pimp'])


@router.post("/create", tags=['Создание'])
async def create(body: Pimp, db_session: AsyncSession = Depends(get_session)) -> PimpDB:
    return await PimpService.create(body, db_session)


@router.get("/get_all", tags=['Получить всё'])
async def get_all(db_session: AsyncSession = Depends(get_session)) -> list[PimpDB]:
   return await PimpService.get_all(db_session)


@router.get("/get${uid}", tags=['Получить одно'])
async def get_one(uid: UUID4, db_session: AsyncSession = Depends(get_session)) -> PimpDB:
   return await PimpService.delete_one(uid, db_session)


@router.put("/update", tags=['Обновить одно'])
async def update_one(uid: UUID4, body: PimpUpdate, db_session: AsyncSession = Depends(get_session)) -> PimpDB:
    return await PimpService.update_one(uid, body, db_session)

@router.delete("/delete${uid}", tags=['Удалить один элемент'])
async def delete_one(uid: UUID4, db_session: AsyncSession = Depends(get_session)):
    return await PimpService.delete_one(uid, db_session)


@router.delete("/delete_all", tags=['Удалить всё'])
async def delete_all(db_session: AsyncSession = Depends(get_session)):
    return await PimpService.delete_all(db_session) 
