# Creates the Link class and Table
# Map Columns - SQL Alchemy
# DB Schema expressed in Python

from sqlalchemy import String, Integer, DateTime
from sqlalchemy import func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import datetime


class Base(DeclarativeBase):
    pass


# Any Class that inherits Base automatically gets made to table
# Link class -> Table Link
class Link(Base):
    __tablename__ = "links"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    original_url: Mapped[str] = mapped_column(String, nullable=False)
    short_code: Mapped[str] = mapped_column(
        String, unique=True, index=True, nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    click_count: Mapped[int] = mapped_column(Integer, default=0)
