'''
Aula 107. Nested Context Managers
'''
# É possível se abrir vários context managers ao mesmo tempo.
with open('file1.txt') as file_1, open('file1.txt') as file_2, open('file1.txt') as file_3:
    print(file_1.readlines())
    print(file_2.readlines())
    print(file_3.readlines())

# É possível também se utilizar nested context managers.
with open('file1.txt') as file_1:
    with open('file2.txt') as file_2:
        with open('file3.txt') as file_3:
            print(file_1.readlines())
            print(file_2.readlines())
            print(file_3.readlines())

