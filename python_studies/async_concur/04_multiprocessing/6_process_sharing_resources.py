'''
Sometimes we wish that multiple processes share resources. The package 
multiprocessing has some tools that help to accomplish this goal.
'''
import ctypes
import multiprocessing
import time


def func_1(value: int, status: bool) -> None:
    if status.value: # status is a ctypes object and its value is a attribute from the object.
        result = value.value + 10
        status.value = False
    else:
        result = value.value + 20
        value.value = 200
        status.value = True
    print(f"func_1 result = {result}")
    time.sleep(0.1)


def func_2(value: int, status: bool) -> None:
    if status.value:
        result = value.value + 30
        status.value = False
    else:
        result = value.value + 40
        value.value = 400
        status.value = True
    print(f"func_2 result = {result}")
    time.sleep(0.1)


def main():
    value = multiprocessing.Value(ctypes.c_int,1000) # The Value class deals only with c types.
    status = multiprocessing.Value(ctypes.c_bool,False)
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
if __name__=='__main__':
    main()
