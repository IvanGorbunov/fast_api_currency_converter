from datetime import datetime, UTC
from typing import Optional

from sqlalchemy import ForeignKey, Column, Integer, Float, DateTime
from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped, relationship

from .base import Base


class Currency(Base):
    __tablename__ = "currency"

    code: Mapped[str] = mapped_column(String(3), unique=True, index=True)


class CurrencyRate(Base):
    __tablename__ = "currency_rate"

    currency_code_id: Mapped[int] = mapped_column(ForeignKey("currency.id"), index=True)
    currency_code: Mapped["Currency"] = relationship(back_populates="currency_rates")

    rate: Mapped[Optional[float]] = mapped_column(Float(), nullable=True)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        # default_factory=lambda: datetime.now(UTC),
        default=datetime.now(UTC),
        onupdate=datetime.now(UTC),
    )
