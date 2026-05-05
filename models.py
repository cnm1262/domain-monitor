from sqlalchemy import Column, Integer, String, Float
from database import Base

class Domain(Base):
    __tablename__ = "domains"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, unique=True, index=True)
    owner_email = Column(String)
    status = Column(String, default="UNKNOWN")
    response_time = Column(Float, default=0)
    last_checked = Column(String, default="")