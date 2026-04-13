from fastapi.routing import APIRouter

from fastapi import HTTPException

from pydantic import UUID4
from src.schemas.client_whore import ClientWhore, ClientWhoreDB, ClientWhoreUpdate
from src.models.client_whore import ClientsWhoreSQL

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete, update

from src.db.session import get_session
from src.service.client import ClientService
from src.service.whore import WhoreService


class ClientWhoreService:
    model = ClientsWhoreSQL

    @classmethod
    async def create(cls, body: ClientWhore, db_session) -> ClientWhoreDB:
        await ClientService.get_one(body.client_uid, db_session)
        await WhoreService.get_one(body.whore_uid, db_session)
        new_obj = cls.model(**body.model_dump())
        db_session.add(new_obj)
        await db_session.commit()
        return new_obj


    @classmethod
    async def get_all(cls, db_session) -> list[ClientWhoreDB]:
        query = select(cls.model)
        query_result = await db_session.execute(query)
        return query_result.scalars().all()

    @classmethod
    async def get_one(cls, uid: UUID4, db_session) -> ClientWhoreDB:
        query = select(cls.model)
        query = query.where(cls.model.uid == uid)
        query_result = await db_session.execute(query)
        result = query_result.scalars().first()
        if result == None:
            raise HTTPException(404, "Встреча не запланирована!")
        return result
    
    @classmethod
    async def update_one(cls, uid: UUID4, body: ClientWhoreUpdate, db_session) -> ClientWhoreDB:
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
        return 'Запись встречи клиента и шлюхи успешно удалена!'


    @classmethod
    async def delete_all(cls, db_session):
        query = delete(cls.model)
        await db_session.execute(query)
        await db_session.commit()
        return 'Записи встречи клиента и шлюхи успешно удалены!'
