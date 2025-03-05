from sqlalchemy import ForeignKey, Column, Integer, String, MetaData, Table,create_engine
from sqlalchemy.orm import relationship, backref,sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import text



convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

engine = create_engine('sqlite:///freebies.db')

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base(metadata=metadata)

#company model class
class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    founding_year = Column(Integer())

    #many to many rel with Dev using Freebie as the junction table
    devs = relationship('Dev', secondary = 'freebies', backref = 'companies')
    
    #one to many rel with Freebie
    freebies = relationship('Freebie', backref = 'company')

    def __repr__(self):
        return f'<Company {self.name}>'
    
    #giving out freebies 
    def give_freebie(self,dev,item_name,value):
        new_freebie = Freebie(item_name = item_name, value=value, dev = dev, company = self)
        session.add(new_freebie)
        session.commit()
        return new_freebie
    #method to get the earliest founded company
    @classmethod
    def oldest_company(cls):
        old_company = session.query(cls).order_by(cls.founding_year).first()
        return old_company
    


#Dev class model
class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer(), primary_key=True)
    name= Column(String())

    #one to many relationship with Freebie
    freebies = relationship('Freebie', backref = 'dev')


    def __repr__(self):
        return f'<Dev {self.name}>'
    
    def received_one(self,item_name):
        for freebie in self.freebies:
            if freebie.item_name == item_name:
                return True
        return False
    
    def give_away(self,dev,freebie):
        if freebie.dev == self:
            freebie.dev = dev
            session.commit()



 #Freebie class model      
class Freebie(Base):
    __tablename__ = 'freebies'

    id = Column(Integer(), primary_key= True)
    item_name = Column(String())
    value = Column(Integer())
    dev_id = Column(Integer(),ForeignKey('devs.id'))
    company_id = Column(Integer(),ForeignKey('companies.id'))

    def __repr__(self):
        return f'<Freebie {self.item_name} - Value: {self.value}>'
    
    def print_details(self):
        return f"{self.dev.name} owns a {self.item_name} from {self.company.name}."

    
Base.metadata.create_all(engine)


