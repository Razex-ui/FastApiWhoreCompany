import uuid
from sqlalchemy import UUID
from sqlalchemy import String, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from src.db.session import Base

from datetime import datetime


class WhoresSQL(Base):
    __tablename__ = 'whores'

    uid: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    email: Mapped[str] = mapped_column(String, nullable=False)
    address: Mapped[str] = mapped_column(String, nullable=False)
    phone_number: Mapped[str] = mapped_column(String, nullable=False)
    pimp_uid: Mapped[str] = mapped_column(UUID, ForeignKey("pimps.uid", ondelete="CASCADE"), nullable=False)
    update_time: Mapped[datetime] = mapped_column(DateTime, onupdate=datetime.now(), default=datetime.now())
