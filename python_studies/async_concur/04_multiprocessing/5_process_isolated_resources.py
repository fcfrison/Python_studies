"""
By default Python processes don't share resources. They are kind of
isolated from each other. The bellow code tries to show this isolation.
"""
import multiprocessing
import time


def func_1(value: int, status: bool) -> None:
    print(hex(id(value)))
    if status:
        result = value + 10
        status = False
    else:
        result = value + 20
        value = 200
        status = True
    print(f"func_1 result = {result}")
    time.sleep(0.1)


def func_2(value: int, status: bool) -> None:
    print(hex(id(value)))
    if status:
        result = value + 30
        status = False
    else:
        result = value + 40
        value = 400
        status = True
    print(f"func_2 result = {result}")
    time.sleep(0.1)


def main():
    value = 1000
    status = False
    print(hex(id(value)))
    p1 = multiprocessing.Process(# Apesar de 'value' apontar para a mesma ref de memória da var no escopo global
                            target=func_1, # por serem processos diferentes, não há alteração de valor.
                            kwargs={"value": value, "status": status}
    )
    p2 = multiprocessing.Process(
        target=func_2, kwargs={"value": value, "status": status}
    )

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print(value)
if __name__=='__main__':
    main()
