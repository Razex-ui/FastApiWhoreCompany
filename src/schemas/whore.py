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
