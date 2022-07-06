# *z conterá td o que estiver especificado no lado esquerdo da igualdade.
# # Em outras palavras,  '*z' representa o resto. 
x,y, w, *z = list(range(1,50))
print(x)
print(y)
print(w)
print(z)

x,*y =tuple(range(1,20))
print(x)
print(y)

a, *b = 'Felipe Conzatti Frison'
print(a)
print(b)

# É possível se adicionar '*rótulo' entre outras variávies. 
x,*w, z = list(range(1,50))
print(x)
print(w)
print(z)


# O operador * também pode ser utilizado no lado direito da igualdade. 
# Nesse caso, ele apenas irá desempacotar os valores do iterável.
l1 = [1,2,3]
l2 = [4,5,6]
l=[*l1,*l2]
print(l)

dict_1 = {'a':1, 'b':2, 'c':3}
dict_2 = {'c':1, 'd':5, 'a':8}
lista = [*dict_1, *dict_2]
conjunto = {*dict_1, *dict_2}
print(lista)
print(conjunto)


# O operador ** no desempacotamento: esse operador pode ser utilizado para 
# desempacotar dicionários, considerando o par chave:valor. Chaves repetidas
# não serão mantidas, nesse caso.
dict_3 = {'x':1, 'y':2, 'w':3}
dict_4 = {'c':5, 'f':9, 'z':8}
dict_5 = {'q':1, 'w':32, 'ea':8}
dict_6 = {**dict_3, **dict_4, **dict_5}


# Nested unpacking.
l = [1,2,[3,4]]
a,b,(c,d) = l
print(a)
print(b)
print(c)
print(d)

a, *b, (c,*d)=[1,2,3,'felipe']
