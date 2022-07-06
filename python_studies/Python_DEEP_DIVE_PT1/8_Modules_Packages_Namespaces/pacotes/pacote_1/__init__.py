'''
Código do pacote: 'pacote_1'.
'''
# Ao se executar Python no terminal e inserir 'pacote_1.__file__', será retornado
# o local em que se encontra o código do módulo, ou seja, o local em que se 
# encontra '__init__.py'.
# O código que segue abaixo só foi colocado aqui por questões pedagógicas. Em 
# outras palavras, __init__.py não precisaria ter esse código. 
'''
import pacote_1
pacote_1.__file__
# Se quisermos verificar a que pacote '__init.py__' está associado, receberemos 
# como retorno 'pacote_1'. 
pacote_1.__package__
# Para se verificar o diretório em que se encontra o 'pacote_1'. 
pacote_1.__path__
'''

'''
Quando é efetuada uma importação do tipo:
"import pacote_1.pacote_1_1.modulo_1_1a"
o que ocorre é:
1) É criado um espaço na memória para 'pacote_1', sendo que tal endereço é referenciado 
no system cache(no dicionário sys.modules, na verdade), e 'pacote_1' também é armazenado
no espaço global de variáveis. Após isso, 'pacote_1.__init__.py' é executado.
2) É criado um espaço na memória para 'pacote_1.pacote_1_1', sendo que tal endereço é referenciado 
no system cache(no dicionário sys.modules, na verdade). 
Após isso, 'pacote_1.pacote_1_1.__init__.py' é executado.
3) É criado um espaço na memória para 'pacote_1.pacote_1_1.modulo_1_1a', sendo 
que tal endereço é referenciado no system cache(no dicionário sys.modules, na verdade). 
Após isso, 'pacote_1.pacote_1_1.modulo_1_1a.py' é executado.
Outra coisa é:
Ao se fazer "import pacote_1.pacote_1_1", o módulo 'modulo_1_1a.py' não é importado. Ou seja, 
não existirá uma referência a esse módulo nem em sys.modules, nem no espaço global do módulo.
Moral da história: ao se importar um pacote, não estão se importando os subpacotes e módulos
ligados ao mesmo. 
Vamos imaginar que eu deseje, ao fazer a importação de um pacote, que todos os módulos existentes
nele sejam importados, nesse caso, uma medida possível seria se "colocar" os 'imports' dos 
módulos no arquivo '__init__.py' do pacote importado.
'''
print('Executando pacote_1.__init__.py')
valor = 'pacote_1 - valor'