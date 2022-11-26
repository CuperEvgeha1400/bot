from sqlalchemy import Table, Index, Integer, String, Column, Text, \
                       DateTime, Boolean, PrimaryKeyConstraint, \
                       UniqueConstraint, ForeignKey
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

#123123123123123
@as_declarative()
class Base:
    @declared_attr
    def __tablename__(self):
        return self.__name__
    id = Column(Integer, primary_key=True)
    created = Column(DateTime, default=datetime.now, server_default='NOW()')


class User(Base):
    tgId = Column(Integer, nullable=False)
    Name = Column(String, nullbase=False)


class Role(Base):
    role = Column(String, nullbase=False)
    userId = Column(Integer, nullbase=False)


class QuestionAnswer(Base):
    question = Column(String, nullbase=False)
    answer = Column(String, nullbase=False)
    qa = relationship("Question")

class SessionLog(Base):
    user_id = Column(Integer, ForeignKey('User.id'), nullable=False)
    algorithm = Column(String, nullable=False)
    successful = Column(Boolean, nullable=False)


class Question(Base):
    question = Column(String, ForeignKey("QuestionAnswer.question"))
