from pydantic import BaseModel, Field, UUID4


class CharacteristicsWhore(BaseModel):
    characteristic_uid: UUID4 = Field(description="Uid характеристики", default=None)
    whore_uid: UUID4 = Field(description="Uid шлюхи", default=None)


class CharacteristicsWhoreUpdate(BaseModel):
    characteristic_uid: UUID4 | None = Field(description="Uid характеристики", default=None)
    whore_uid: UUID4 | None = Field(description="Uid шлюхи", default=None)


class CharacteristicsWhoreDB(BaseModel):
    characteristic_uid: UUID4 = Field(description="Uid характеристики", default=None)
    whore_uid: UUID4 = Field(description="Uid шлюхи", default=None)
    uid: UUID4 = Field(default=None)
