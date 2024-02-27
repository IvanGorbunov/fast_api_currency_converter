from datetime import datetime, UTC
from typing import Optional

from sqlalchemy import Float, DateTime, Column, Integer, Table
from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped

from . import db_helper
from .base import Base


currency_rate = Table(
    "role",
    db_helper.metadata,
    Column("id", Integer, primary_key=True),
    Column('code', String(3), index=True),
    Column("name", String(30)),
    Column("rate", Float(), nullable=True),
    Column(
        "updated_at",
        DateTime(timezone=True),
        default=datetime.now(UTC),
        onupdate=datetime.now(UTC),
    ),
)

class CurrencyRate(Base):
    code: Mapped[str] = mapped_column(String(3), index=True)
    name: Mapped[str] = mapped_column(String(30))
    rate: Mapped[Optional[float]] = mapped_column(Float(), nullable=True)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.now(UTC),
        onupdate=datetime.now(UTC),
    )
