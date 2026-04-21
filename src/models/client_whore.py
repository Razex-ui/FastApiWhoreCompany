from datetime import datetime
import uuid
from sqlalchemy import UUID
from sqlalchemy import String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from src.db.session import Base


class ClientsWhoreSQL(Base):
    __tablename__ = "clients_whore"

    uid: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    client_uid: Mapped[uuid.UUID] = mapped_column(UUID, ForeignKey("clients.uid", ondelete="CASCADE"), nullable=False)
    whore_uid: Mapped[uuid.UUID] = mapped_column(UUID, ForeignKey("whores.uid", ondelete="CASCADE"), nullable=False)
    date_of_visit: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    cost_of_visit: Mapped[int] = mapped_column(Integer, nullable=False)
