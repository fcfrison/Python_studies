# Qdo uma função é definida dentro da outra, o escopo da função "por fora" é
# chamado de não local. 
def func_externa():
    # Escopo não local.
    a = 10
    def func_interna():
        # Escopo local
        print(a) 
    func_interna()

func_externa()

# Outro exemplo.
def func_externa_1():
    # Escopo não local.
    a = 10
    def func_interna_1():
        # Escopo local
        a = 100
        print(f'escopo local = {a}') 
    func_interna_1()
    print(f'escopo não local: {a}')

func_externa_1()

# No entanto, é possível se declarar uma variável como não local. 
def func_externa_2():
    # Escopo não local.
    a = 10
    print(a)
    def func_interna_2():
        # Nesse caso, ao declarar nonlocal 'a', esse 'a' será o mesmo que o declarado
        # no escopo não local. 
        nonlocal a
        a = 100
        print(f'escopo local = {a}') 
    func_interna_2()
    print(f'escopo não local: {a}')

func_externa_2()

# A noção de 'non local variable' é buscar o primeiro escopo não local encontrado, 
# não interessando quantos níveis acima esse escopo esteja. Por exemplo:
def outer():
    # escopo não local
    x = 'hello'
    def inner1():
        def inner2():
            # Declarar 'x' como não local faz com que uma variável declarada 
            # dois níveis acima seja alterada. 
            nonlocal x
            x='python'
        inner2()
        print(x)
    inner1()
outer()
