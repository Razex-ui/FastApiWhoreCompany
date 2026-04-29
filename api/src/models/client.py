import uuid
from sqlalchemy import UUID
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from src.db.session import Base


class ClientsSQL(Base):
    __tablename__ = "clients"

    uid: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    phone_number: Mapped[str] = mapped_column(String, nullable=False)
    address: Mapped[str] = mapped_column(String, nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=False)
    referral: Mapped[str] = mapped_column(String, nullable=True)
