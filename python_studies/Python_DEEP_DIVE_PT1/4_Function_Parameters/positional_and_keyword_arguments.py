def funcao_qualquer(a: int, b=1, c=2):
    return a+b+c
# Uma vez passado um argumento nomeado, todos os seguintes deverão também
# sê-lo.
funcao_qualquer(a=5, c=5, b=10)

funcao_qualquer(3,c=5,b=4)