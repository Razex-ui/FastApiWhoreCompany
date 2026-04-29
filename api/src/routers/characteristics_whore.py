from fastapi.routing import APIRouter
from pydantic import UUID4

from src.schemas.characteristics_whore import CharacteristicsWhore, CharacteristicsWhoreUpdate, CharacteristicsWhoreDB, CharacteristicsWhoreFilter

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.session import get_session

from src.service.characteristics_whore import CharacteristicsWhoreService as Service


router = APIRouter()


@router.post("/create", tags=['Создание'])
async def create(body: CharacteristicsWhore, db_session: AsyncSession = Depends(get_session)) -> CharacteristicsWhoreDB:
    return await Service.create(body, db_session)


@router.post("/get_with_filter", tags=['Отфильтровать'])
async def get_filter(filter_by: CharacteristicsWhoreFilter, db_session: AsyncSession = Depends(get_session)) -> list[CharacteristicsWhoreDB]:
    return await Service.get_with_filter(filter_by, db_session)


@router.get("/get_all", tags=['Получить всё'])
async def get_all(db_session: AsyncSession = Depends(get_session)) -> list[CharacteristicsWhoreDB]:
    return await Service.get_all(db_session)


@router.get("/get${uid}", tags=['Получить одно'])
async def get_one(uid: UUID4, db_session: AsyncSession = Depends(get_session)) -> CharacteristicsWhoreDB:
    return await Service.get_one(uid, db_session)


@router.put("/update", tags=['Обновить одно'])
async def update_one(uid: UUID4, body: CharacteristicsWhoreUpdate, db_session: AsyncSession = Depends(get_session)) -> CharacteristicsWhoreDB:
    return await Service.update_one(uid, body, db_session)


@router.delete("/delete${uid}", tags=['Удалить один элемент'])
async def delete_one(uid: UUID4, db_session: AsyncSession = Depends(get_session)):
    return await Service.delete_one(uid, db_session)


@router.delete("/delete_all", tags=['Удалить всё'])
async def delete_all(db_session: AsyncSession = Depends(get_session)):
    return await Service.delete_all(db_session)
