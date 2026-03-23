import uuid
from sqlalchemy import UUID
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from src.db.session import Base


class type_of_whores(Base):
    __tablename__ = "type"

    uid: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String, nullable=False)
