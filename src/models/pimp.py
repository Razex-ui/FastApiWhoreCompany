import uuid
from sqlalchemy import UUID
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from src.db.session import Base


class PimpsSQL(Base):
    __tablename__ = "pimps"

    uid: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    number: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False)
    discord: Mapped[str] = mapped_column(String, nullable=True)
    nickname: Mapped[str] = mapped_column(String, unique=True)
