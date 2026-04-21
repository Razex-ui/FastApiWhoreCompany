from fastapi import HTTPException

from pydantic import UUID4
from src.schemas.characteristics_whore import CharacteristicsWhore, CharacteristicsWhoreUpdate, CharacteristicsWhoreDB, CharacteristicsWhoreFilter
from src.models.characteristics_whore import CharacteristicsWhoreSQL

from sqlalchemy import select, delete, update


class CharacteristicsWhoreService:
    model = CharacteristicsWhoreSQL
    out_schema = CharacteristicsWhoreDB

    @classmethod
    async def create(cls, body: CharacteristicsWhore, db_session) -> out_schema:
        new_obj = cls.model(**body.model_dump())
        db_session.add(new_obj)
        await db_session.commit()
        return new_obj

    @classmethod
    async def get_with_filter(cls, filter_by: CharacteristicsWhoreFilter, db_session) -> list[out_schema]:
        query = select(cls.model)

        if filter_by.limit > -1:
            query = query.limit(filter_by.limit)
        if filter_by.offset > 0:
            query = query.offset(filter_by.offset)
        
        if filter_by.whore_uid is not None:
            query = query.where(cls.model.pimp_uid == filter_by.whore_uid)

        if filter_by.characteristic_uid is not None:
            query = query.where(cls.model.characteristic_uid == filter_by.characteristic_uid)

        query_result = await db_session.execute(query)
        return query_result.scalars().all()

    @classmethod
    async def get_all(cls, db_session) -> list[out_schema]:
        query = select(cls.model)
        query_result = await db_session.execute(query)
        return query_result.scalars().all()

    @classmethod
    async def get_one(cls, uid: UUID4, db_session) -> out_schema:
        query = select(cls.model)
        query = query.where(cls.model.uid == uid)
        query_result = await db_session.execute(query)
        result = query_result.scalars().first()
        if result == None:
            raise HTTPException(404, "Характеристика у шлюхи не найдена!")
        return result

    @classmethod
    async def update_one(cls, uid: UUID4, body: CharacteristicsWhoreUpdate, db_session) -> out_schema:
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
        return 'Характеристика шлюхи успешно удалена!'

    @classmethod
    async def delete_all(cls, db_session):
        query = delete(cls.model)
        await db_session.execute(query)
        await db_session.commit()
        return 'Характеристики шлюх успешно удалены!'
