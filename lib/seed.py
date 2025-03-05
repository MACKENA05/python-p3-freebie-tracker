# # !/usr/bin/env python3

# # Script goes here!
from models import Company,Dev, Freebie,session,Base,engine
from models import session
from sqlalchemy.sql import text

Base.metadata.create_all(engine)

session.execute(text('PRAGMA foreign_keys = ON'))

#clearing existing data
session.query(Freebie).delete()
session.query(Company).delete()
session.query(Dev).delete()

#creating instances of company
company1 = Company(name='BallersTech', founding_year= 2018)
company2 = Company(name='CrimackSoln', founding_year = 2020)
company3 = Company (name= 'Alpha solution', founding_year=2025)

#creating instances of dev
dev1 = Dev(name='Cris Jeff')
dev2 = Dev(name='Ann Mercy')
dev3 = Dev(name = 'Monicah Mackena')


#creating instances of freebies
freebie1 = Freebie(item_name = 'Notebooks',value = 15, dev = dev1,company=company1)
freebie2 = Freebie(item_name = 'Tshirts', value = 20, dev=dev1, company = company2)
freebie3 = Freebie(item_name="Wristbands", value=10, dev=dev2, company=company2)
freebie4 = Freebie(item_name="Water Bottle", value=15, dev=dev2, company=company3)
freebie5 = Freebie(item_name="Stickers", value=25, dev=dev3, company=company1)


#adding to database and saving
session.add_all([company1, company2, company3, dev1, dev2, dev3, freebie1, freebie2, freebie3, freebie4])

session.commit()

print('Data added successfuly')