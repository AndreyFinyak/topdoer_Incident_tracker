from enum import Enum
from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import (
    Integer,
    Text,
    DateTime,
    Enum as EnumOrm
)


class IncidentStatus(str, Enum):
    new = "new"
    investigating = "investigating"
    resolved = "resolved"
    closed = "closed"
    ignored = "ignored"


class IncidentSource(str, Enum):
    operator = "operator"
    monitoring = "monitoring"
    partner = "partner"
    other = "other"


class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True


class IncidentORM(Base):
    __tablename__ = 'incidents'

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True
    )
    body: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )
    status: Mapped[IncidentStatus] = mapped_column(
        EnumOrm(IncidentStatus),
        nullable=False,
        default=IncidentStatus.new
    )
    source: Mapped[IncidentSource] = mapped_column(
        EnumOrm(IncidentSource),
        nullable=False,
        default=IncidentSource.other
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=datetime.utcnow()
    )
