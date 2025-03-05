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

print('Devs who have collected freebies from {company.name}:')
for dev in company.devs:
    print({dev.name})

freebie = session.query(Freebie).filter_by(item_name= 'Notebooks').first()

print(f"Freebie \n (Item name:{freebie.item_name} \n Item value:{freebie.value} ")
print(f"Collected by Dev: {freebie.dev.name}")
print(f"Provided  by Company: {freebie.company.name}")


# if __name__ == '__main__':
#     engine = create_engine('sqlite:///freebies.db')
#     import ipdb; ipdb.set_trace()
