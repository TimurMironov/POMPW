from datetime import datetime
from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, DateTime, ForeignKey, JSON, Boolean, Float

from backend_services.services.tables.base_table import Base


class User(Base):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    personal_info: Mapped[Optional["PersonalInfo"]] = relationship(back_populates="user", cascade="all, delete-orphan", uselist=False)
    contact: Mapped[Optional["Contact"]] = relationship(back_populates="user", cascade="all, delete-orphan", uselist=False)
    employment: Mapped[Optional["Employment"]] = relationship(back_populates="user", cascade="all, delete-orphan", uselist=False)
    education: Mapped[Optional["Education"]] = relationship(back_populates="user", cascade="all, delete-orphan", uselist=False)
    settings: Mapped[Optional["Settings"]] = relationship(back_populates="user", cascade="all, delete-orphan", uselist=False)
    statistics: Mapped[Optional["Statistics"]] = relationship(back_populates="user", cascade="all, delete-orphan", uselist=False)

class PersonalInfo(Base):
    __tablename__ = 'personal_info'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    first_name: Mapped[str] = mapped_column(String(30), nullable=False)
    last_name: Mapped[str] = mapped_column(String(30), nullable=False)
    middle_name: Mapped[Optional[str]] = mapped_column(String(30))
    birth_date: Mapped[str] = mapped_column(String)
    age: Mapped[int] = mapped_column(Integer)

    user: Mapped[User] = relationship(back_populates="personal_info", uselist=False)

class Contact(Base):
    __tablename__ = 'contact'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    email: Mapped[str] = mapped_column(String(30), nullable=False)
    phone: Mapped[str] = mapped_column(String(30), nullable=False)
    address: Mapped[dict] = mapped_column(JSON)
    networks: Mapped[list[dict]] = mapped_column(JSON)

    user: Mapped[User] = relationship(back_populates="contact", uselist=False)

class Employment(Base):
    __tablename__ = 'employment'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    position: Mapped[str] = mapped_column(String(30), nullable=False)
    company: Mapped[dict] = mapped_column(JSON)
    experience: Mapped[int] = mapped_column(Integer, nullable=False)
    remote: Mapped[bool] = mapped_column(Boolean)

    user: Mapped[User] = relationship(back_populates="employment", uselist=False)

class Education(Base):
    __tablename__ = 'education'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    level: Mapped[str] = mapped_column(String(30), nullable=False)
    institution: Mapped[str] = mapped_column(String(30))
    faculty: Mapped[str] = mapped_column(String(30))
    graduation_year: Mapped[str] = mapped_column(String(30), nullable=False)
    degree: Mapped[str] = mapped_column(String(30))

    user: Mapped[User] = relationship(back_populates="education", uselist=False)

class Settings(Base):
    __tablename__ = 'settings'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    is_active: Mapped[bool] = mapped_column(nullable=False) # В модели isActive надо поменять
    notifications: Mapped[dict] = mapped_column(JSON)
    privacy: Mapped[dict] = mapped_column(JSON, nullable=False)

    user: Mapped[User] = relationship(back_populates="settings", uselist=False)

class Statistics(Base):
    __tablename__ = 'statistics'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    registration_date: Mapped[datetime] = mapped_column(DateTime)
    last_login: Mapped[datetime] = mapped_column(DateTime)
    login_count: Mapped[int] = mapped_column(Integer)
    rating: Mapped[float] = mapped_column(Float)

    user: Mapped[User] = relationship(back_populates="statistics", uselist=False)
