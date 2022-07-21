'''

There is a strong relationship between tasks and futures. In fact, task directly inherits
from future. A future can be thought as representing a value that we won’t have for
a while. A task can be thought as a combination of both a coroutine and a future.
When we create a task, we are creating an empty future and running the coroutine.
Then, when the coroutine has completed with either an exception or a result, we set
the result or exception of the future.
'''

