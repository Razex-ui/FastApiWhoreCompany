from fastapi.routing import APIRouter
from pydantic import UUID4
from src.schemas.characteristics import Characteristics, CharacteristicsUpdate, CharacteristicsDB, CharacteristicsFilter  
from src.models.characteristics import CharacteristicsSQL

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete, update

from src.db.session import get_session


from src.service.characteristics import CharacteristicsService


router = APIRouter(prefix="/characteristics", tags=['Characteristics'])


@router.post("/create", tags=['Создание'])
async def create(body: Characteristics, db_session: AsyncSession = Depends(get_session)) -> CharacteristicsDB:
    return await CharacteristicsService.create(body, db_session)


@router.post("/get_with_filter", tags=['Отфильтровать'])
async def get_filter(filter_by: CharacteristicsFilter, db_session: AsyncSession = Depends(get_session)) -> list[CharacteristicsDB]:
    return await CharacteristicsService.get_with_filter(filter_by, db_session)


@router.get("/get_all", tags=['Получить всё'])
async def get_all(db_session: AsyncSession = Depends(get_session)) -> list[CharacteristicsDB]:
    return await CharacteristicsService.get_all(db_session)


@router.get("/get${uid}", tags=['Получить одно'])
async def get_one(uid: UUID4, db_session: AsyncSession = Depends(get_session)) -> CharacteristicsDB:
    return await CharacteristicsService.get_one(uid, db_session)

@router.put("/update", tags=['Обновить одно'])
async def update_one(uid: UUID4, body: CharacteristicsUpdate, db_session: AsyncSession = Depends(get_session)) -> CharacteristicsDB:
    return await CharacteristicsService.update_one(uid, body, db_session)


@router.delete("/delete${uid}", tags=['Удалить один элемент'])
async def delete_one(uid: UUID4, db_session: AsyncSession = Depends(get_session)):
    return await CharacteristicsService.delete_one(uid, db_session)

@router.delete("/delete_all", tags=['Удалить всё'])
async def delete_all(db_session: AsyncSession = Depends(get_session)):
    return await CharacteristicsService.delete_all(db_session)