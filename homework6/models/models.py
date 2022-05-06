from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text

Base = declarative_base()


class TotalAmountRequestsModel(Base):
    __tablename__ = 'TotalAmountRequests'
    id = Column(Integer, primary_key=True, autoincrement=True)
    number = Column(Integer, nullable=False)


class AmountByTypeRequestsModel(Base):
    __tablename__ = 'AmountByTypeRequests'
    id = Column(Integer, primary_key=True, autoincrement=True)
    method = Column(String(8), nullable=False)
    number = Column(Integer, nullable=False)


class Top10FrequentRequestsModel(Base):
    __tablename__ = 'Top10FrequentRequests'
    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(Text, nullable=False)
    number = Column(Integer, nullable=False)


class Top5LargestRequestsWithClientErrorModel(Base):
    __tablename__ = 'Top5LargestRequestsWithClientError'
    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(Text, nullable=False)
    code = Column(Integer, nullable=False)
    size = Column(Integer, nullable=False)
    ip = Column(String(16), nullable=False)


class Top5FrequentRequestsWithServerErrorModel(Base):
    __tablename__ = 'Top5FrequentRequestsWithServerError'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ip = Column(String(16), nullable=False)
    number = Column(Integer, nullable=False)
