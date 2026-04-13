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
