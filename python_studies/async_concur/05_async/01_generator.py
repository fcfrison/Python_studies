'''
Generator review.

Code related to the course "rogramação Concorrente e Assíncrona com Python". 
Available at https://www.udemy.com/course/programacao-concorrente-e-assincrona-com-python/
'''

from typing import Generator

def fibonacci()->Generator[int,None,None]:
    value : int = 0
    proximo : int = 1
    while True:
        value, proximo = proximo, value + proximo
        yield value

f_1 = fibonacci()

for n in f_1:
    if n>100:
        break
    print(n)


