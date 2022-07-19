'''
It's possible to create a echo socket server using asyncio.

The code below was created by Matthew Fowler in the book 'Python 
Concurrency with asyncio-Manning Publications (2022)'. 
'''

import asyncio
import socket
from asyncio import AbstractEventLoop

async def echo(connection: socket,
                loop: AbstractEventLoop) -> None:
    '''
    This coroutine is responsible for receive data from the clients and 
    send data back to the clients.
    '''
    while (data := await loop.sock_recv(connection, 1024)): # if data is received from a client connection, 
                                                            # then data is send back to the client
        await loop.sock_sendall(connection, data) 

async def listen_for_connection(server_socket: socket, loop: AbstractEventLoop):
    while True:
        connection, address = await loop.sock_accept(server_socket) # given that the OS notification system is 
                                                                    # used by asyncio, the sock_accept coroutine will return
                                                                    # someting when a connection requests has been made
        connection.setblocking(False)
        print(f"Got a connection from {address}")
        asyncio.create_task(echo(connection, loop)) # wraps the echo coroutine for each connection that we get 

async def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create the server socket
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_address = ('127.0.0.1', 8000) # create the address
    server_socket.setblocking(False) # turning methods (like accept() and recv) that by default are blocking into non-blocking
    server_socket.bind(server_address)
    server_socket.listen() # server socket starts to listen
    await listen_for_connection(server_socket, asyncio.get_event_loop())

asyncio.run(main())