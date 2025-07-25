# backend/models/models.py

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from ..database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)

    folders = relationship("Folder", back_populates="owner")
    qrs = relationship("QR", back_populates="owner")


class Folder(Base):
    __tablename__ = "folders"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)

    owner = relationship("User", back_populates="folders")
    qrs = relationship("QR", back_populates="folder")


class QR(Base):
    __tablename__ = "qrs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)  # 'text', 'url', 'pdf'
    content = Column(Text, nullable=False)
    image_url = Column(String)
    folder_id = Column(Integer, ForeignKey("folders.id"), nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)

    folder = relationship("Folder", back_populates="qrs")
    owner = relationship("User", back_populates="qrs")
