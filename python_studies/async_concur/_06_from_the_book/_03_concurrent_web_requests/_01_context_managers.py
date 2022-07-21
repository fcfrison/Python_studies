'''
Instead of wrap the code inside a try/except block, it's possible
to use asynchronous context managers.

Below, follows the implementation of such kind of context managers. 
As in the other sections, we remain using the example of sockets.

The code below was created by Matthew Fowler in the book 'Python 
Concurrency with asyncio-Manning Publications (2022)'. 
'''

import asyncio
import socket
from types import TracebackType
from typing import Optional, Type

class ConnectedSocket:
    def __init__(self, server_socket):
        self._connection = None
        self._server_socket = server_socket
    
    async def __aenter__(self):
        '''
        This coroutine is called when we enter the with block. It 
        waits until a client connects and returns the connection.
        '''
        print('Entering context manager, waiting for connection')
        loop = asyncio.get_event_loop() # create an event loop
        connection, address = await loop.sock_accept(self._server_socket) # 
        self._connection = connection
        print('Accepted a connection')
        return self._connection

    
    async def __aexit__(self,
                        exc_type: Optional[Type[BaseException]],
                        exc_val: Optional[BaseException],
                        exc_tb: Optional[TracebackType]):
        '''
        This coroutine is called when we exit the with block. In it,
        we clean up any resources we use. In this case, we close the 
        connection.
        '''
        print('Exiting context manager')
        self._connection.close()
        print('Closed connection')

async def main():
    loop = asyncio.get_event_loop()
    server_socket = socket.socket()
    server_socket.setsockopt(socket.SOL_SOCKET, 
                            socket.SO_REUSEADDR, 1)
    server_address = ('127.0.0.1', 9000)
    server_socket.setblocking(False)
    server_socket.bind(server_address)
    server_socket.listen()
    async with ConnectedSocket(server_socket) as connection:# calling__aenter__ 
        data = await loop.sock_recv(connection, 1024)
        print(data) # here, the method __aexit__ is called.

asyncio.run(main())
    