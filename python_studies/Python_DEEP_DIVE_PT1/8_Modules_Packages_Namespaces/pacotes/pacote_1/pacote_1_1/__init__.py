print('executando pacote_1_1.')
valor = 'pacote_1_1 - valor'
'''
Aula 138
Ao se executar no terminal 'import pacote_1.pacote_1_1', registra-se no dicionário
sys.modules o endereço de memória de 'pacote_1' e de 'pacote_1.pacote_1_1'. 
Além disso, é importado para o namespace global o endereço de memória de 'pacote_1'.
Por isso, qualquer referencia ao pacote_1_1 deve ser efetuada através de pacote_1.
Caso fosse de meu interesse invocar diretamente 'pacote_1_1' no terminal, então
eu poderia fazer algo como 'from pacote_1 import pacote_1_1'. Vamos imaginar que 
eu escrevesse essa linha de comando antes de qualquer coisa. Nesse caso, ao executar
esse comando, eu teria as seguintes consequências:
1) seria criado um espaço de memória para 'pacote_1', o qual passaria seria referenciado
no dicionário sys.module (ou seja, no 'system cache'). 
2) seria criado um espaço de memória para 'pacote_1.pacote_1_1', o qual passaria 
seria referenciado no dicionário sys.module (ou seja, no 'system cache'). 
3) seria criada uma referência a 'pacote_1_1' no 'namespace' global. Ou seja, 
as referências a 'pacote_1_1' deveriam ser efetuadas diretamente. 
OBS.: relembrando que o espaço global das variáveis para um determinado módulo 
pode ser verificado através de globals().
4) quando é 
'''