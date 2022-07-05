#The use of multiple threads can be dangerous, because the same resources 
# are shared. Therefore, some cautions are necessary. In the following script,
# some consistency errors arrise, due to the way resources are shared on Python. 

import threading
import random
import time

from pydantic import BaseModel, Field
from typing import List
from decimal import Decimal

class BankAccount(BaseModel):
    saldus: Decimal = Field(0,gt=0)


def main():
    
    accounts = [BankAccount(saldus=Decimal(random.randint(5_000,10_000))) 
                for _ in range(5)]
    total = sum(account.saldus for account in accounts)
    jobs = [
        threading.Thread(target = services, args= (accounts,total)),
        threading.Thread(target = services, args= (accounts,total)),
        threading.Thread(target = services, args= (accounts,total)),
        threading.Thread(target = services, args= (accounts,total)),
        threading.Thread(target = services, args= (accounts,total)),
        threading.Thread(target = services, args= (accounts,total))
    ]
    [job.start() for job in jobs]
    [job.join() for job in jobs]
    
    print("The job is done")
    bank_validation(accounts,total)

def services(accounts : List, total : Decimal):
    '''
    Function that call the transfer values function
    and then call the validation function.
    '''
    for _ in range(1,10):
        c1, c2 = random.sample(accounts,2)
        value = Decimal(random.randint(1,15))
        transfer(c1,c2,value)
        bank_validation(accounts, total)


def transfer(source:BankAccount,target:BankAccount,value:Decimal):
    '''
    Functions that transfers values between different bank accounts. 
    '''
    print("iniciando thread!!!!!")
    if source.saldus < value:
        return 
    source.saldus -= value
    time.sleep(0.1)
    target.saldus += value


def bank_validation(accounts: List[BankAccount], total:Decimal):
    '''
    This function checks for inconsistencies on transfered values 
    between bank accounts.
    '''
    sum_agr = sum(account.saldus for account in accounts)
    if total!=sum_agr:
        print(f'ERROR: {total}!={sum_agr}')
    else:
        print(f'OK: {total}=={sum_agr}')
if __name__=='__main__':
    main()