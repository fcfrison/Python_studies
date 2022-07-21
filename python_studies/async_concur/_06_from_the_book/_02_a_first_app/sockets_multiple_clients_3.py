'''
Creating a server that echoes back messages sent by clients. 
This application is highly efficient, because it uses the 
OS notification system.

The code below was created by Matthew Fowler in the book 'Python 
Concurrency with asyncio-Manning Publications (2022)'. 
'''
import selectors
import socket
from selectors import SelectorKey
from typing import List, Tuple
selector = selectors.DefaultSelector() # create an instance of a selector, allowing the use of OS notification system 
server_socket = socket.socket()
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_address = ('127.0.0.1', 8000)
server_socket.setblocking(False) # make methods like 'accept' and 'recv' non-blocking
server_socket.bind(server_address)
server_socket.listen()

selector.register(server_socket, selectors.EVENT_READ) # register the server_socket in the OS notification system
while True:
    events: List[Tuple[SelectorKey, int]] = selector.select(timeout=5) # create a selector for monitoring events, which 
                                                                        # returns when an event occurs
    if len(events) == 0:
        print('No events, waiting a bit more!')
    for event, _ in events:
        event_socket = event.fileobj # the fileobj is an object that is related to the OS API of the notification system  
        if event_socket == server_socket: # if this condition happens, then we have a connection attempt
            connection, address = server_socket.accept() # create a new (client) socket
            connection.setblocking(False) # setting the connection as non-blocking
            print(f"I got a connection from {address}")
            selector.register(connection, selectors.EVENT_READ) # register the client socket in the OS notification system
        else:
            data = event_socket.recv(1024)
            print(f"I got some data: {data}")
            event_socket.send(data)