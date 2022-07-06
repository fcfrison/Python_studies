import sys
print('Executando main.py -- nome do módulo: {0}'.format(__name__))
print('-------------------------------------------\n\n')

# Como eu estava tendo problemas de importação ao 'pressionar' 'shift + enter', 
# inseri o caminho absoluto de 'exemplo_1' como um dos locais em que o Python procura
# os módulos a serem executados. 
print(sys.path.append(
    'c:\\Users\\fcfri\\Estudos_Python\\Curso_Deep_Dive_Python_Part_I\\8_Modules_Packages_Namespaces\\exemplo_1'))

# Quando um módulo é importado, ele é executado. 
import modulo_1
