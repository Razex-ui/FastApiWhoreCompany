from pydantic import BaseModel, Field, UUID4


class ClientWhore(BaseModel):
    date_of_visit: str = Field(description="Дата встречи", default=None)
    cost_of_visit: int = Field(description="Цена встречи", default=None)
    whore_uid: UUID4 = Field(description="Uid шлюхи", default=None)
    client_uid: UUID4 = Field(description="Uid клиента", default=None)


class ClientWhoreUpdate(BaseModel):
    date_of_visit: str | None = Field(description="Дата встречи", default=None)
    cost_of_visit: int | None = Field(description="Цена встречи", default=None)
    whore_uid: UUID4 | None = Field(description="Uid шлюхи", default=None)
    client_uid: UUID4 | None = Field(description="Uid клиента", default=None)


class ClientWhoreDB(BaseModel):
    uid: UUID4 = Field(description="uid")
    date_of_visit: str = Field(description="Дата встречи", default=None)
    cost_of_visit: int = Field(description="Цена встречи", default=None)
    whore_uid: UUID4 = Field(description="Uid шлюхи", default=None)
    client_uid: UUID4 = Field(description="Uid клиента", default=None) 