from pydantic import BaseModel, Field, UUID4


class Pimp(BaseModel):
    number: str = Field(
        default=None,
        description="Номер телефона (E.164 формат)",
        examples=["+79131234567"]
    )
    email: str = Field(description="Email", default=None)
    discord: str = Field(description="Дискорд сутенера")
    nickname: str = Field(description="Прозвище сутенера")


class PimpUpdate(BaseModel):
    number: str | None = Field(
        default=None,
        description="Номер телефона (E.164 формат)",
        examples=["+79131234567"]
    )
    email: str | None = Field(description="Email", default=None)
    discord: str | None = Field(description="Дискорд сутенера", default=None)
    nickname: str | None = Field(description="Прозвище сутенера", default=None)

    
class PimpDB(BaseModel):
    uid: UUID4 = Field(description="Pimp uid")
    number: str = Field(
        default=None,
        description="Номер телефона (E.164 формат)",
        examples=["+79131234567"]
    )
    email: str = Field(description="Email", default=None)
    discord: str = Field(description="Дискорд сутенера")
    nickname: str = Field(description="Прозвище сутенера")


class PimpFilter(BaseModel):
    limit: int = Field(description="Лимит вывода", default=-1, ge=-1)
    offset: int = Field(description="Смещение вывода", default=0, ge=0)
    search_query: str | None = Field(description="Поисковая строка", default=None)
