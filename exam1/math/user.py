from sqlalchemy import Column, Integer, String
from connect import Base


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    score = Column(Integer)

    def __str__(self):
        return "{} - {}".format(self.name, self.score)

    def __repr__(self):
        return self.__str__()