from datetime import date

from pydantic import BaseModel, Field
 



class ParticipantGet(BaseModel):
    id : int =""
    itn : int =""
    name : str =""
    form : str =""
    adress : str = ""

    class Config:
        orm_mode = True

class ContractDebitGet(BaseModel):
    itn : int = ""
    facilit : str	=""
    contract : str	=""
    debt : float

    class Config:
        orm_mode = True



 # Функция расчёта задолности по Контракту
def debt_cotract(pay, docs):
    costs = pay.groupby(['contactor', 'object', 'contract']).agg({'sum': 'sum'})
    done = docs.groupby(['contactor', 'object', 'contract']).agg({'sum': 'sum'})
    other = contract.data.groupby('contract').agg({'gu': 'sum', 'gp': 'sum'})
    result = done.apply(lambda x: x*(1-other.gu-other.gp))- costs
    result = result.dropna(axis=0)
    return result

class ContractGet(BaseModel):
    id : int
    num : str
    date : date
    itn : ParticipantGet
    price : float
    facility : str
    our_template : int 
    gu : float
    gp : float
    prepayment : float

    class Config:
        orm_mode = True