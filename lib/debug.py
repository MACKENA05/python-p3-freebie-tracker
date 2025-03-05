#!/usr/bin/env python3

import ipdb

from sqlalchemy import create_engine

from models import Company, Dev, Freebie,session

dev = session.query(Dev).filter_by(name='Cris Jeff').first()

print(f"Name: {dev.name}")

print(f'companies where {dev.name} has collected freebies')
for company in dev.companies:
    print({company.name})


company = session.query(Company).filter_by(name='BallersTech').first()
print(F"Company: {company.name}")

print(f"Devs who have collected freebies from {company.name}:")
for dev in company.devs:
    print({dev.name})

freebie = session.query(Freebie).filter_by(item_name= 'Notebooks').first()

print(f"Freebie \n (Item name:{freebie.item_name} \n Item value:{freebie.value} ")
print(f"Collected by Dev: {freebie.dev.name}")
print(f"Provided  by Company: {freebie.company.name}")

#Testing aggregate methods

# Test Freebie.print_details()
freebie = session.query(Freebie).first()
print(freebie.print_details())  

#testing company give_freebie()
company = session.query(Company).first()
dev = session.query(Dev).first()
new_freebie = company.give_freebie(dev,'Bags',2)
print(new_freebie)

#Testing the oldest company()
print(Company.oldest_company())

#Test Dev received one()
dev = session.query(Dev).first()
print(dev.received_one("Notebook"))

#testing give_away
dev1 = session.query(Dev).first()
dev2 = session.query(Dev).filter_by(name= 'Ann Mercy').first()
freebie = session.query(Freebie).first()
dev1.give_away(dev2,freebie)
print(freebie.dev.name)