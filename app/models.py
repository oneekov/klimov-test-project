from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text
from sqlalchemy import Enum as SQLEnum

import enum

class SexEnum(str, enum.Enum):
    MALE = 'мужчина'
    FEMALE = 'женщина'

class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True
    __table_args__ = {'schema': 'klimov'}

class Admin(Base):
    __tablename__ = 'admins'

    admin_id = Column(Integer, primary_key=True)
    username = Column(String(32), unique=True, nullable=False)
    password_hash = Column(String(60), nullable=False)
    is_super_admin = Column(Boolean, nullable=False, default=False)

# class Test(Base):
#     __tablename__ = 'tests'

#     test_id = Column(Integer, primary_key=True)
#     name = Column(Text, nullable=False)
#     created_by = Column(Integer, ForeignKey('klimov.admins.admin_id'), nullable=False)

class Answer(Base):
    __tablename__ = 'answers'

    answer_id = Column(Integer, primary_key=True)
    # test_id = Column(Integer, ForeignKey('klimov.tests.test_id'), nullable=True)

    user_agent = Column(Text, nullable=True)
    ip = Column(Text, nullable=False)

    sex = Column(SQLEnum(SexEnum), nullable=False)
    age = Column(Integer, nullable=False)

    surname = Column(String(48), nullable=False)
    name = Column(String(48), nullable=False)
    patronymic = Column(String(48), nullable=True)

    nature_points = Column(Integer, nullable=False)
    tech_points = Column(Integer, nullable=False)
    human_points = Column(Integer, nullable=False)
    sign_points = Column(Integer, nullable=False)
    image_points = Column(Integer, nullable=False)
