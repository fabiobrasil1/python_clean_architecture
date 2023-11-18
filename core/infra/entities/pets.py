from sqlalchemy import Column, String, Integer, Enum, ForeignKey
from core.infra.config import Base
import enum
from sqlalchemy.orm import relationship

class AnimalsTypes(enum.Enum):
    dog = "dog"
    cat = "cat"
    fish = "fish"
    turtle = "turtle"


class Pets(Base):
    """Pets Entity"""

    __tablename__ = 'pets'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False, unique=True)
    specie = Column(Enum(AnimalsTypes), nullable=False)
    age = Column(Integer)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("Users", back_populates="pets")
    
    def __rep__(self):
        return f"Pet: [name={self.name}, specie={self.specie}, age={self.age}, user_id={self.user_id}]"