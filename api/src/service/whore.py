from fastapi.routing import APIRouter

from fastapi import HTTPException

from pydantic import UUID4
from src.schemas.whore import Whore, WhoreUpdate, WhoreDB, WhoreFilter
from src.models.whore import WhoresSQL

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete, update, or_

from src.db.session import get_session


class WhoreService:
    model = WhoresSQL

    @classmethod
    async def create(cls, body: Whore, db_session) -> WhoreDB:
        new_obj = cls.model(**body.model_dump())
        db_session.add(new_obj)
        await db_session.commit()
        return new_obj
    
    @classmethod
    async def get_with_filter(cls, filter_by: WhoreFilter, db_session) -> list[WhoreDB]:
        query = select(cls.model)

        if filter_by.limit > -1:
            query = query.limit(filter_by.limit)
        if filter_by.offset > 0:
            query = query.offset(filter_by.offset)
        
        if filter_by.search_query is not None:
            query = query.where(
                or_(
                    cls.model.email.ilike(f'{filter_by.search_query}'),
                    cls.model.address.ilike(f'{filter_by.search_query}'),
                    cls.model.phone_number.ilike(f'{filter_by.search_query}')
                )
            )

        if filter_by.pimp_uid is not None:
            query = query.where(cls.model.pimp_uid == filter_by.pimp_uid)

        if filter_by.update_time_from is not None:
            query = query.where(
                cls.model.update_time >= filter_by.update_time_from
            )
        if filter_by.update_time_to is not None:
            query = query.where(
                cls.model.update_time <= filter_by.update_time_to
            )

        query_result = await db_session.execute(query)
        return query_result.scalars().all()


    @classmethod
    async def get_all(cls, db_session) -> list[WhoreDB]:
        query = select(cls.model)
        query_result = await db_session.execute(query)
        return query_result.scalars().all()

    @classmethod
    async def get_one(cls, uid: UUID4, db_session) -> WhoreDB:
        query = select(cls.model)
        query = query.where(cls.model.uid == uid)
        query_result = await db_session.execute(query)
        result = query_result.scalars().first()
        if result == None:
            raise HTTPException(404, "Шлюха не найдена!")
        return result

    @classmethod
    async def update_one(cls, uid: UUID4, body: WhoreUpdate, db_session) -> WhoreDB:
        query = update(cls.model)
        query = query.where(cls.model.uid == uid)
        query = query.values(**body.model_dump(exclude_unset=True))
        await db_session.execute(query)
        await db_session.commit()

        return await cls.get_one(uid, db_session)

    @classmethod
    async def delete_one(cls,uid: UUID4, db_session):
        query = delete(cls.model)
        query = query.where(cls.model.uid == uid)
        await db_session.execute(query)
        await db_session.commit()
        return 'Шлюха успешно удалена!'

    @classmethod
    async def delete_all(cls, db_session):
        query = delete(cls.model)
        await db_session.execute(query)
        await db_session.commit()
        return 'Шлюхи успешно удалены!'
