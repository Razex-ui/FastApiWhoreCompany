from pydantic import BaseModel, Field, UUID4


class Client(BaseModel):
    address: str = Field(description="Адрес", default=None)
    phone_number: str = Field(
        default=None,
        description="Номер телефона (E.164 формат)",
        examples=["+79131234567"])
    name: str = Field(description="Имя")
    referral: str = Field(description="Реферал")


class ClientUpdate(BaseModel):
    address: str | None = Field(description="Адрес", default=None)
    phone_number: str | None = Field(
        default=None,
        description="Номер телефона (E.164 формат)",
        examples=["+79131234567"])
    name: str | None = Field(description="Имя", default=None)
    referral: str | None = Field(description="Реферал", default=None)


class ClientDB(BaseModel):
    uid: UUID4 = Field(description="Uid клиента")
    address: str = Field(description="Адрес", default=None)
    phone_number: str = Field(
        default=None,
        description="Номер телефона (E.164 формат)",
        examples=["+79131234567"])
    name: str = Field(description="Имя клиента")
    referral: str = Field(description="Реферал")
    

class ClientFilter(BaseModel):
    limit: int = Field(description="Лимит вывода", default=-1, ge=-1)
    offset: int = Field(description="Смещение вывода", default=0, ge=0)
    # Поисковая строка.
    search_query: str | None = Field(description="Поисковая строка", default=None)