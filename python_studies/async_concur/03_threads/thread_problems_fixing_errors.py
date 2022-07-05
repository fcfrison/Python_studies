# In this section, the problems related to shared resources are handled. 
import threading
import random
import time

from pydantic import BaseModel, Field
from typing import List
from decimal import Decimal

lock = threading.RLock() # Criando uma instância de uma lock. A 'lock' deverá ser 
                         # inserida sempre que houver recursos compartilhados entre as threads.

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
    for _ in range(1,1000):
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
    # Como a realizaçao de transferências utiliza recursos comuns (as ref. de memória são comuns) entre as threads, u
    # utilizar uma lock.
    with lock:
        source.saldus -= value
        time.sleep(0.01)
        target.saldus += value


def bank_validation(accounts: List[BankAccount], total:Decimal):
    '''
    This function checks for inconsistencies on transfered values 
    between bank accounts.
    '''
    with lock:
        sum_agr = sum(account.saldus for account in accounts)
    if total!=sum_agr:
        print(f'ERROR: {total}!={sum_agr}')
    else:
        print(f'OK: {total}=={sum_agr}')
if __name__=='__main__':
    main()