# Conditional expression.
# A conditional expression tem a seguinte "cara":
'''
X if (condition is true) else Y
'''
# A conditional expression que vira abaixo equivale ao que seguinte:
a=25
if a<5:
    print("a<5")
else:
    print("a>=5")

print("a<5") if a<5 else print("a>=5") 
