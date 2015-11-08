# coding: utf-8
from sqlalchemy import BigInteger, Column, Date, DateTime, Integer, SmallInteger, String, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func


Base = declarative_base()
metadata = Base.metadata


class Item(Base):
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True)
    projectid = Column(Integer, index=True)
    itemparentid = Column(Integer, )
    priority = Column(Integer, )
    context = Column(String(80), )
    title = Column(String(80), )
    description = Column(String(700), )
    deadlinedate = Column(Date, )
    memberid = Column(Integer, index=True)
    authorid = Column(Integer, )


class ItemComment(Base):
    __tablename__ = 'itemcomment'

    itemcommentid = Column(BigInteger, primary_key=True)
    itemid = Column(Integer, index=True)
    memberid = Column(Integer, )
    postdate = Column(DateTime(timezone=True), )
    body = Column(String(400), )
    lastchangedate = Column(DateTime(timezone=True), )


class ItemStatus(Base):
    __tablename__ = 'itemstatus'

    itemstatusid = Column(BigInteger, primary_key=True)
    itemid = Column(Integer, index=True)
    statusdate = Column(DateTime(timezone=True), )
    statuskey = Column(Integer, )
    memberid = Column(Integer, )


class Member(Base):
    __tablename__ = 'member'

    memberid = Column(Integer, primary_key=True)
    email = Column(String(120), )
    title = Column(String(20), )
    firstname = Column(String(50), )
    lastname = Column(String(50), )
    city = Column(String(60), )
    countryid = Column(String(2), )
    phone = Column(String(30), )
    username = Column(String(20), index=True)
    password = Column(String(60), )
    salt = Column(String(8), )
    autologin = Column(Integer, )
    timezone = Column(SmallInteger, )
    expirationdate = Column(DateTime(timezone=True), )
    lastlogindate = Column(DateTime(timezone=True), )
    lastloginaddress = Column(String(60), )
    creationdate = Column(DateTime(timezone=True), )
    lastchangedate = Column(DateTime(timezone=True), )
    visits = Column(Integer, )
    badaccess = Column(Integer, )
    level = Column(Integer, )
    activation = Column(String(16), )
    authorid = Column(Integer, )
    enabled = Column(Integer, )


class MemberProject(Base):
    __tablename__ = 'memberproject'

    memberid = Column(Integer, primary_key=True, )
    projectid = Column(Integer, primary_key=True, )
    position = Column(Integer, )


class Project(Base):
    __tablename__ = 'project'

    projectid = Column(Integer, primary_key=True)
    name = Column(String(120), )
    description = Column(String, )


class ProjectStatus(Base):
    __tablename__ = 'projectstatus'

    projectstatusid = Column(Integer, primary_key=True)
    projectid = Column(Integer, index=True)
    statusdate = Column(DateTime(timezone=True), )
    statuskey = Column(Integer, )
    memberid = Column(Integer, )

from db_url import *
from sqlalchemy import create_engine
the_bind = create_engine(two)
metadata.create_all(bind=the_bind)
