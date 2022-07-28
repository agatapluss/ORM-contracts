from sqlalchemy.orm import Session
from typing import List


from database import SessionLocal
from models import Contract, Participant, Payment, Document
from schemas import ContractDebitGet, ContractGet, ParticipantGet

from fastapi import FastAPI, Depends

app = FastAPI()

def get_db():
    with SessionLocal() as db:
        return db


@app.get("/contract/all", response_model=List[ContractGet])
def all_contracts(db : Session = Depends(get_db)):
    return db.query(Contract).all()

@app.get("/", response_model = ContractDebitGet)
def debt_cotract():
    costs = pay.groupby(['contactor', 'object', 'contract']).agg({'sum': 'sum'})
    done = docs.groupby(['contactor', 'object', 'contract']).agg({'sum': 'sum'})
    other = contract.data.groupby('contract').agg({'gu': 'sum', 'gp': 'sum'})
    result = done.apply(lambda x: x*(1-other.gu-other.gp))- costs
    result = result.dropna(axis=0)
    return result

@app.get("/payment/all")
def all_payment(db : Session = Depends(get_db)):
    return db.query(Payment).all()