from sqlalchemy import Column, String, Integer
from core.infra.config import Base
from sqlalchemy.orm import relationship

class Users(Base):
    """ Users Entity"""
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True )
    password = Column(String, nullable=False)
    pets = relationship("Pets", back_populates="user", uselist=True)

    def __rep__(self):
        return f"Usr [name={self.name}]"
