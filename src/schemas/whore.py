from pydantic import BaseModel, Field, UUID4
from pydantic_extra_types.phone_numbers import PhoneNumber 

class WhoreData(BaseModel):
    uid: UUID4 = Field(description="User uid")
    email: str = Field(description="Email", default=None)
    address: str = Field(description="Адрес", default=None)
    phone_number: str = Field(
        default=None,
        description="Номер телефона (E.164 формат)",
        examples=["+79131234567"]
    )

