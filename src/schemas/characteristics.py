from pydantic import BaseModel, Field, UUID4


class Characteristics(BaseModel):
    name: str = Field(description="Название характеристики")


class CharacteristicsUpdate(BaseModel):
    name: str | None = Field(description="Название характеристики")    


class CharacteristicsDB(BaseModel):
    name: str = Field(description="Название характеристики")
    uid: UUID4 = Field(description="uid характеристики", default=None)


class CharacteristicsFilter(BaseModel):
    limit: int = Field(description="Лимит вывода", default=-1, ge=-1)
    offset: int = Field(description="Смещение вывода", default=0, ge=0)
    search_query: str | None = Field(description="Поисковая строка", default=None)
