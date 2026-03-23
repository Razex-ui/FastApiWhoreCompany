from fastapi.routing import APIRouter
from schemas.whore import WhoreData
from models.whore import Whore

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete

from db.session import engine, get_session


router = APIRouter(prefix="/whore", tags=['Whore'])


@router.post("/create")
async def create(body: WhoreData, db_session: AsyncSession = Depends(get_session)) -> WhoreData:
    new_whore = Whore(**body.model_dump())
    db_session.add(new_whore)
    await db_session.commit()
    return new_whore

@router.get("/get_all")
async def get_all(db_session: AsyncSession = Depends(get_session)) -> list[WhoreData]:
    query = select(Whore)
    query_result = await db_session.execute(query)
    return query_result.scalars().all()


@router.delete("/delete_all")
async def delete_all(db_session: AsyncSession = Depends(get_session)):
    query = delete(Whore)
    await db_session.execute(query)
    await db_session.commit()

#
# запрос -> коммит/роллбек
#
# 10000000  00000000 00000000 00000001 #
