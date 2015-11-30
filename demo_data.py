# coding: utf-8
from schema import *
from db_url import *
import datetime
from sqlalchemy import create_engine
the_bind = create_engine(two)
from sqlalchemy.orm import Session
s = Session(the_bind)

p = Project()
p.name = "Development"
p.description = "Tasks for the dev team"

p2 = Project()
p2.name = "Testing"
p2.description = "Tests tasks"

p3 = Project()
p3.name = "Cooking"
p3.description = "What should we eat this week?"

s.add(p)
s.add(p2)
s.add(p3)
s.commit()
s.refresh(p)
s.refresh(p2)
s.refresh(p3)

i = Item()
i.projectid = p.projectid
i.priority = 4
i.title = "Do the code"
i.description = "ALANJKAHSDJAHSJKDH Ƣ\nƢƢƢƢ"
i.deadlinedate = datetime.datetime.utcnow()
s.add(i)

i2 = Item()
i2.projectid = p2.projectid
i2.title = "TESTSTSTSTSTSTESTTEST"
i2.description = "Ĉ ĉ Ċ ċ\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nEND"
s.add(i2)

i3 = Item()
i3.projectid = p3.projectid
i3.title = "Find a delicious recipe"
i3.description = "FInd a delicious recipe and <strong>coooook</strong> it"
s.add(i3)

s.commit()

m = Member()
m.username = "Mike the Mechanic"
m.admin = False
s.add(m)

m2 = Member()
m2.username = "Joe Jackson"
m2.admin = False
s.add(m2)

s.commit()

s1 = ItemStatus()
s1.itemid = 1
s1.statusdate = datetime.datetime.today()
s1.statuskey = 2
s1.memberid = 1

s.add(s1)
s.commit()

s2 = ItemStatus()
s2.itemid = 2
s2.statusdate = datetime.datetime.today()
s2.statuskey = 3
s2.memberid = 1

s.add(s2)
s.commit()

c7 = ItemComment()
c7.itemid = 1
c7.body = "Comment via SQLAlchemy"
c7.postdate = datetime.datetime.utcnow()
c7.memberid = 1

s.add(c7)
s.commit()

cristian = Member()
cristian.username = "cristian"
cristian.admin = True
s.add(cristian)
s.commit()
s.refresh(cristian)

mp = MemberProject()
mp.memberid = cristian.memberid
mp.projectid = p.projectid
mp.position = 1

s.add(mp)
s.commit()

mp = MemberProject()
mp.memberid = cristian.memberid
mp.projectid = p3.projectid
mp.position = 2

s.add(mp)
s.commit()

mp = MemberProject()
mp.memberid = cristian.memberid
mp.projectid = p2.projectid
mp.position = 3

s.add(mp)
s.commit()
