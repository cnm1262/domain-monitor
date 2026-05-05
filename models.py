from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from database import Base

class Domain(Base):
    __tablename__ = "domains"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, unique=True, index=True)
    status = Column(String, default="UNKNOWN")
    response_time = Column(String, default="0")
    last_checked = Column(DateTime, default=datetime.utcnow)