from datetime import datetime

from pydantic import BaseModel, Field, UUID4


class ClientWhore(BaseModel):
    date_of_visit: datetime = Field(description="Дата встречи", default=None)
    cost_of_visit: int = Field(description="Цена встречи", default=None)
    whore_uid: UUID4 = Field(description="Uid шлюхи", default=None)
    client_uid: UUID4 = Field(description="Uid клиента", default=None)


class ClientWhoreUpdate(BaseModel):
    date_of_visit: datetime | None = Field(description="Дата встречи", default=None)
    cost_of_visit: int | None = Field(description="Цена встречи", default=None)
    whore_uid: UUID4 | None = Field(description="Uid шлюхи", default=None)
    client_uid: UUID4 | None = Field(description="Uid клиента", default=None)


class ClientWhoreDB(BaseModel):
    uid: UUID4 = Field(description="uid")
    date_of_visit: datetime = Field(description="Дата встречи", default=None)
    cost_of_visit: int = Field(description="Цена встречи", default=None)
    whore_uid: UUID4 = Field(description="Uid шлюхи", default=None)
    client_uid: UUID4 = Field(description="Uid клиента", default=None) 


class ClientWhoreFilter(BaseModel):
    limit: int = Field(description="Лимит вывода", default=-1, ge=-1)
    offset: int = Field(description="Смещение вывода", default=0, ge=0)
    whore_uid: UUID4 | None = Field(description="Uid шлюхи", default=None)
    client_uid: UUID4 | None = Field(description="Uid клиента", default=None)

    date_of_visit_from: datetime | None = Field(description="Дата встречи", default=None)
    date_of_visit_to: datetime | None = Field(description="Дата встречи", default=None)

    cost_of_visit_from: int | None = Field(description="Цена встречи", default=None)
    cost_of_visit_to: int | None = Field(description="Цена встречи", default=None)