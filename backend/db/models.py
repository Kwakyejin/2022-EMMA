from sqlalchemy import Column, Integer, String, Text, DateTime
from db.database import Base
class Person(Base):
    __tablename__ = "Person"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    intro = Column(Text, nullable=True)
    Interest = Column(Text, nullable=True)
    Qual = Column(Text, nullable=True)
    Major = Column(Text, nullable=True)
    Competition = Column(Text, nullable=True)
    #status = Column(String, nullable=False)
    #result = Column(Text, nullable=True)
    #start_date = Column(DateTime, nullable=False)
    #end_date = Column(DateTime, nullable=True)