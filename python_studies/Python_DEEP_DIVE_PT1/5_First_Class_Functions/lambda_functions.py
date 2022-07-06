# Funções lambda pode ser "armazenadas" em variáveis.
fn = lambda x: x**2
print(id(fn))
print(hex(id(fn)))

# É possível chamar a função.
fn(3)

# É possível se atribuirem valores padrão para os parâmetros.
fn_1 = lambda x=20,y=10: x+y
fn_1(y=30)

# É possível, inclusive, utilizar-se *args e *args.
fn_2 = lambda x, *args: [(x,item) for item in args]
fn_2(5,'p','y','t','h','o','n')

# É possível também se utilizarem **kwrgs.
fn_3 = lambda *args,**kwargs: print([args,{**kwargs}])
fn_3(2,5,3,6,a=654,b=365)

# Funções lambdas podem ser passadas como argumento para outras funções. 
def apply_func(x, fn):
    print(fn(x))

apply_func(2,lambda x:x**2)

# Outro exemplo.
def apply_func(fn,*args,**kwargs):
    return fn(*args,**kwargs)
apply_func(lambda x:x**2,3)
apply_func(lambda x,y:x+y,2,3)