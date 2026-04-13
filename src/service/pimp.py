from fastapi.routing import APIRouter
from pydantic import UUID4
from src.schemas.pimp import Pimp, PimpDB, PimpUpdate
from src.models.pimp import PimpsSQL

from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete, update

from src.db.session import get_session


class PimpService:
    model = PimpsSQL

    @classmethod
    async def create(cls, body: Pimp, db_session) -> PimpDB:
        new_obj = cls.model(**body.model_dump())
        db_session.add(new_obj)
        await db_session.commit()
        return new_obj


    @classmethod
    async def get_all(cls, db_session) -> list[PimpDB]:
        query = select(cls.model)
        query_result = await db_session.execute(query)
        return query_result.scalars().all()


    @classmethod
    async def get_one(cls, uid: UUID4, db_session) -> PimpDB:
        query = select(cls.model)
        query = query.where(cls.model.uid == uid)
        query_result = await db_session.execute(query)
        result = query_result.scalars().first()
        if result == None:
            raise HTTPException(404, "Сутенёр не найдена!")
        return result

    @classmethod
    async def update_one(cls, uid: UUID4, body: PimpUpdate, db_session) -> PimpDB:
        query = update(cls.model)
        query = query.where(cls.model.uid == uid)
        query = query.values(**body.model_dump(exclude_unset=True))
        await db_session.execute(query)
        await db_session.commit()
        
        return await cls.get_one(uid, db_session)
   
    @classmethod
    async def delete_one(cls, uid: UUID4, db_session):
        query = delete(cls.model)
        query = query.where(cls.model.uid == uid)
        await db_session.execute(query)
        await db_session.commit()
        return 'Сутенер опущен!'


    @classmethod
    async def delete_all(cls, db_session):
        query = delete(cls.model)
        await db_session.execute(query)
        await db_session.commit()
        return 'Сутенеры опущены!'