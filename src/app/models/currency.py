from datetime import datetime, UTC
from typing import Optional

from sqlalchemy import Float, DateTime
from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped

from .base import Base


class CurrencyRate(Base):
    code: Mapped[str] = mapped_column(String(3), index=True)
    name: Mapped[str] = mapped_column(String(30))
    rate: Mapped[Optional[float]] = mapped_column(Float(), nullable=True)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.now(UTC),
        onupdate=datetime.now(UTC),
    )
