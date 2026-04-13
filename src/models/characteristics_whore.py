import uuid
from sqlalchemy import UUID
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from src.db.session import Base


class CharacteristicsWhoreSQL(Base):
    __tablename__ = "characteristics_whore"

    uid: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    whore_uid: Mapped[uuid.UUID] = mapped_column(UUID, ForeignKey("whores.uid"), nullable=False)
    characteristic_uid: Mapped[uuid.UUID] = mapped_column(UUID, ForeignKey("characteristics.uid"), nullable=False)
