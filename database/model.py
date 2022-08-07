from sqlalchemy import Column, Float, Integer, String,DateTime,ForeignKey
from sqlalchemy.orm import declarative_base,relationship

from database.base import Base
import datetime

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

class PreUnderwritingData(Base):
    __tablename__ = "preunderwriting"
    id = Column(Integer, primary_key=True)
    memberID = Column(String, nullable=False)
    dateOfBirth = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    height = Column(Integer, nullable=False)
    weight = Column(Integer, nullable=False)
    bmi = Column(Integer, nullable=False)
    smoker = Column(String, nullable=False)
    occupationID = Column(String, nullable=False)
    createdate = Column(DateTime, default=datetime.datetime.now)
    healthscore = relationship('HealthScore', back_populates='healthscore', lazy='dynamic', order_by='desc(HealthScore.value)')

class HealthScore(Base):
    __tablename__ = "healthscore"
    id = Column(Integer, primary_key=True)
    scoreName = Column(String, nullable=False)
    value = Column(Integer, nullable=False)
    healthscore_id = Column(Integer, ForeignKey('healthscore.id'))