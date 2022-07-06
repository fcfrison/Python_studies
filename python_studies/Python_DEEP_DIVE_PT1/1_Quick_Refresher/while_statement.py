# while True -> fica ciclando até que um break ocorra. Afinal de contas, 
# a condição True é sempre verdadeira. 
i=0
while True:
    print(i)
    i+=1
    if i>=3:
        break

# while...else -> se o while chegar ao fim sem a ocorrência de um break, então
# o else será executado.
l =[1,2]
val=10
idx=0
while idx<len(l):
    if l[idx]==val:
        break
    idx=idx+1
else: # Se a condição l[idx]==val não for satisfeita, então o while loop chegará a um fim e, após isso, entrará aqui.
    l.append(val)
print(l)

# try..else...finally
a=5
b=0
try:
    print(a/b)
except ZeroDivisionError:
    print("Divisão por zero.")
finally:
    print("Essa parte do try sempre executará.")

# loop for ...
for i,j in [(0,1),(2,3),(4,5)]:
    print(i,j)

# É possível a utilização de break dentro de loop for.
for idx in range(1,5):
    if idx%4==0:
        break
    print(idx)

# É possível também a utilização de continue.
for idx in range(1,6):
    if idx%4==0:
        continue
    print(idx)

# for ... else
for idx in range(1,6):
    if idx%7==0:
        print("Múltiplo de 7")
        break
    print(idx)
else:
    print("Não há múltiplos de 7.")

