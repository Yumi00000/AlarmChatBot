from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False)
    uChat_id = Column(String, unique=True, nullable=False)

    def __repr__(self):
        return f"User(id={self.id}, uChat_id={self.uChat_id})"


class Channels(Base):
    __tablename__ = "channels"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    channelTG_id = Column(String, nullable=False)
    uChat_id = Column(Integer, ForeignKey("uChat_id"))

    def __repr__(self):
        return f"<Channels(id={self.id}, name={self.name})>"


class KeyWords(Base):
    __tablename__ = "keywords"
    id = Column(Integer, primary_key=True)
    keyword = Column(String)
    uChat_id = Column(Integer, ForeignKey("uChat_id"))
    channel_id = Column(Integer, ForeignKey("channels.id"))
