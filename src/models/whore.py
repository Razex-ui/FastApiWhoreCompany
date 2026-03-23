import uuid
from sqlalchemy import UUID
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from src.db.session import Base


class Whore(Base):
    __tablename__ = 'whore'

    uid: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    email: Mapped[str] = mapped_column(String, nullable=False)
    address: Mapped[str] =  mapped_column(String, nullable=False)
    phone_number: Mapped[str] =  mapped_column(String, nullable=False)
