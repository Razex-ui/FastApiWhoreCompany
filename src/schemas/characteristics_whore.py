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

class CharacteristicsWhoreFilter(BaseModel):
    limit: int = Field(description="Лимит вывода", default=-1, ge=-1)
    offset: int = Field(description="Смещение вывода", default=0, ge=0)
    characteristic_uid: UUID4 | None = Field(description="Uid характеристики", default=None)
    whore_uid: UUID4 | None = Field(description="Uid шлюхи", default=None)