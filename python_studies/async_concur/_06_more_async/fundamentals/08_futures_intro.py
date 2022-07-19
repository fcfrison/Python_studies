'''
Studying futures. 
By definition a future is:
"(...) a Python object that contains a single value that you expect to get at some
point in the future but may not yet have". 
'''

from asyncio import Future

my_future = Future() # instantiating a future. In this point in time, there's only the expectation of a value.
print(f'Is my_future done? {my_future.done()}')

my_future.set_result(42) # setting up the value of the future. 
print(f'Is my_future done? {my_future.done()}')
print(f'What is the result of my_future? {my_future.result()}') # my_future.result() will throw an exception if the future result is not setted.