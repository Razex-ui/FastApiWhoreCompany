from pydantic import BaseModel, Field, UUID4


class Characteristics(BaseModel):
    name: str = Field(description="Название характеристики")


class CharacteristicsUpdate(BaseModel):
    name: str | None = Field(description="Название характеристики")    


class CharacteristicsDB(BaseModel):
   name: str = Field(description="Название характеристики")
   uid: UUID4 = Field(description="uid характеристики", default=None) 