
from sqlalchemy import ForeignKey, create_engine, Column, Integer, DateTime, String, Float
from database import Base, engine, SessionLocal
from sqlalchemy.orm import relationship

class Participant(Base):
    __tablename__ = "participant"
    itn = Column(Integer, primary_key = True,  unique=True)
    name = Column(String)
    form = Column(String)
    adress = Column(String)


class Contract(Base):
    __tablename__= "contract"
    id = Column(Integer, primary_key=True, name = "contract_id")
    num = Column(String, name ="num_contr")
    date = Column(DateTime, name = "date_contr")
    itn = Column(Integer, ForeignKey("participant.itn"), primary_key = True)
    it = relationship("Participant")
    price = Column(Float)
    facility = Column(String)
    our_template = Column(Integer)
    gu = Column(Float)
    gp = Column(Float)
    prepayment = Column(Float)



class Payment(Base):
    __tablename__ = "payment"
    id = Column(Integer, unique=True, name = "pay_id")
    date = Column(DateTime, name = "date_of_pay")
    sum = Column(Float)
    itn = Column(Integer, ForeignKey("participant.itn"), primary_key = True)
    it = relationship("Participant")
    contact_id = Column(Integer, ForeignKey(Contract.id), primary_key=True, name = "contract_id")


class Document(Base):
    __tablename__="document"
    id = Column(Integer, unique =True, name = "id_doc")
    date = Column(DateTime, name= "date_doc")
    sum = Column(Float)
    itn = Column(Integer,  ForeignKey("participant.part_id"), unique=True, name = "part_id")
    contract_id = Column(Integer, ForeignKey("contract.contract_id"), primary_key=True, name = "contract_id")

if __name__ == "__main__":
    Base.metadata.create_all(engine)