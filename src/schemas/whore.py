from datetime import datetime

from pydantic import BaseModel, Field, UUID4


class Whore(BaseModel):
    email: str = Field(description="Email", default=None)
    address: str = Field(description="Адрес", default=None)
    phone_number: str = Field(
        default=None,
        description="Номер телефона (E.164 формат)",
        examples=["+79131234567"]
    )
    pimp_uid: UUID4 = Field(description="Идентификатор сутенера")


class WhoreUpdate(BaseModel):
    email: str | None = Field(description="Email", default=None)
    address: str | None = Field(description="Адрес", default=None)
    phone_number: str | None = Field(
        default=None,
        description="Номер телефона (E.164 формат)",
        examples=["+79131234567"]
    )
    pimp_uid: UUID4 | None = Field(description="Идентификатор сутенера", default=None)


class WhoreDB(BaseModel):
    uid: UUID4 = Field(description="Whore uid")
    email: str = Field(description="Email", default=None)
    address: str = Field(description="Адрес", default=None)
    phone_number: str = Field(
        default=None,
        description="Номер телефона (E.164 формат)",
        examples=["+79131234567"]
    )
    pimp_uid: UUID4 = Field(description="Идентификатор сутенера")
    update_time: datetime = Field(description="Время обновления", default=None)


class WhoreFilter(BaseModel):
    limit: int = Field(description="Лимит вывода", default=-1, ge=-1)
    offset: int = Field(description="Смещение вывода", default=0, ge=0)
    # Поисковая строка.
    search_query: str | None = Field(description="Поисковая строка", default=None)

    pimp_uid: UUID4 | None= Field(description="Идентификатор сутенера", default=None)

    update_time_from: datetime = Field(description="Время обновления начиная с", default=None)
    update_time_to: datetime = Field(description="Время обновления заканчивая до", default=None)
