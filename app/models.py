from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy import Enum as SQLEnum

import enum

class SexEnum(str, enum.Enum):
    MALE = 'male'
    FEMALE = 'female'

class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True
    __table_args__ = {'schema': 'klimov'}

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)

    username = Column(String(32), unique=True, nullable=False)
    password_hash = Column(String(60), nullable=False)
    is_admin = Column(Boolean, nullable=False, default=False)
    is_super_admin = Column(Boolean, nullable=False, default=False)

    surname = Column(String(48), nullable=True)
    name = Column(String(48), nullable=True)
    patronymic = Column(String(48), nullable=True)

    school = Column(Text, nullable=True)
    grade_number = Column(Integer, nullable=True)
    grade_letter = Column(String(1), nullable=True)

    contact_email = Column(String(128), nullable=True)
    contact_number = Column(String(16), nullable=True)

    sex = Column(SQLEnum(SexEnum), nullable=True)
    age = Column(Integer, nullable=True)

    # TODO: авторизация через госуслуги

    answers = relationship('Answer', cascade='all, delete-orphan')

class Answer(Base):
    __tablename__ = 'answers'

    answer_id = Column(Integer, primary_key=True)
    # test_id = Column(Integer, ForeignKey('klimov.tests.test_id'), nullable=True)

    user_agent = Column(Text, nullable=True)
    ip = Column(Text, nullable=False)

    user_id = Column(Integer, ForeignKey('klimov.users.id'), nullable=False)

    nature_points = Column(Integer, nullable=False)
    tech_points = Column(Integer, nullable=False)
    human_points = Column(Integer, nullable=False)
    sign_points = Column(Integer, nullable=False)
    image_points = Column(Integer, nullable=False)
