'''
Aula 50. Example 3 - Delegating Iterators
'''
# Ao invés de realizar a programação do método especial __iter__ e da 
# classe que gera iteradores, é possível se delegar essa tarefa para 
# a função iter(), que já foi implementada pelo Python. 
import collections
PersonName = collections.namedtuple("PersonName", "first last")
class PersonNames:
    def __init__(self, persons):
        try:
            self._persons = [person.first.capitalize() + ' ' + person.last.capitalize() for person in persons]
        except (TypeError, AttributeError):
            self._persons = []
        
        def __iter__(self):
            '''
            A delegação da iteração ocorre aqui. 
            '''
            return iter(self._persons)