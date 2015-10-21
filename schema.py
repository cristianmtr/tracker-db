# coding: utf-8
from sqlalchemy import BigInteger, Column, Date, DateTime, Integer, SmallInteger, String, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func


Base = declarative_base()
metadata = Base.metadata


class Item(Base):
    __tablename__ = 'item'

    itemId = Column(Integer, primary_key=True)
    projectId = Column(Integer, index=True)
    itemParentId = Column(Integer, )
    priority = Column(Integer, )
    context = Column(String(80), )
    title = Column(String(80), )
    description = Column(String(700), )
    deadlineDate = Column(Date, )
    memberId = Column(Integer, index=True)
    authorId = Column(Integer, )


class ItemComment(Base):
    __tablename__ = 'itemComment'

    itemCommentId = Column(BigInteger, primary_key=True)
    itemId = Column(Integer, index=True)
    memberId = Column(Integer, )
    postDate = Column(DateTime, )
    body = Column(String(400), )
    lastChangeDate = Column(DateTime, )


class ItemStatus(Base):
    __tablename__ = 'itemStatus'

    itemStatusId = Column(BigInteger, primary_key=True)
    itemId = Column(Integer, index=True)
    statusDate = Column(DateTime, )
    statusKey = Column(Integer, )
    memberId = Column(Integer, )


class Member(Base):
    __tablename__ = 'member'

    memberId = Column(Integer, primary_key=True)
    email = Column(String(120), )
    title = Column(String(20), )
    firstName = Column(String(50), )
    lastName = Column(String(50), )
    city = Column(String(60), )
    countryId = Column(String(2), )
    phone = Column(String(30), )
    username = Column(String(20), index=True)
    password = Column(String(60), )
    salt = Column(String(8), )
    autoLogin = Column(Integer, )
    timeZone = Column(SmallInteger, )
    expirationDate = Column(DateTime, )
    lastLoginDate = Column(DateTime, )
    lastLoginAddress = Column(String(60), )
    creationDate = Column(DateTime, )
    lastChangeDate = Column(DateTime, )
    visits = Column(Integer, )
    badAccess = Column(Integer, )
    level = Column(Integer, )
    activation = Column(String(16), )
    authorId = Column(Integer, )
    enabled = Column(Integer, )


class MemberProject(Base):
    __tablename__ = 'memberProject'

    memberId = Column(Integer, primary_key=True, )
    projectId = Column(Integer, primary_key=True, )
    position = Column(Integer, )


class Project(Base):
    __tablename__ = 'project'

    projectId = Column(Integer, primary_key=True)
    name = Column(String(120), )
    description = Column(String, )


class ProjectStatus(Base):
    __tablename__ = 'projectStatus'

    projectStatusId = Column(Integer, primary_key=True)
    projectId = Column(Integer, index=True)
    statusDate = Column(DateTime, )
    statusKey = Column(Integer, )
    memberId = Column(Integer, )

from db_url import *
from sqlalchemy import create_engine
the_bind = create_engine(two)
metadata.create_all(bind=the_bind)
