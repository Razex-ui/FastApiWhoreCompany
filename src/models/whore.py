import uuid
from sqlalchemy import UUID
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from src.db.session import Base


class WhoresSQL(Base):
    __tablename__ = 'whores'

    uid: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    email: Mapped[str] = mapped_column(String, nullable=False)
    address: Mapped[str] = mapped_column(String, nullable=False)
    phone_number: Mapped[str] = mapped_column(String, nullable=False)
    pimp_uid: Mapped[str] = mapped_column(UUID, ForeignKey("pimps.uid"), nullable=False)
