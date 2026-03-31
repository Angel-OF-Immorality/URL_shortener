# Creates the Link class and Table 

from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy import func
from app.database import Base

# Any Class that inherits Base automatically gets made to table
class Link(Base):
    __tablename__ = "links"

    id = Column(Integer, primary_key=True, index=True)
    original_url = Column(String, nullable=False)
    short_code = Column(String, unique=True, index=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    click_count = Column(Integer, default=0)
