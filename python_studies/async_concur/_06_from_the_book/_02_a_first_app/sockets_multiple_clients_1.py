'''
Creating a problematic server that echoes back mesages from clients.
The problem is that both the server socket and the client socket are
blocking, meaning that the methods accept and recv block until they 
receive data. 

The code below was created by Matthew Fowler in the book 'Python 
Concurrency with asyncio-Manning Publications (2022)'. 
'''

import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creating the socket 
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # configuring the socket
server_address = ('127.0.0.1', 8000) 
server_socket.bind(server_address) # binding the socket to the chose server address 
server_socket.listen() # listening to calls

connections = []

try:
    while True:
        connection, client_address = server_socket.accept() # "connection" points to the client connection object
        print(f'I got a connection from {client_address}!')
        connections.append(connection)
        for connection in connections:
            buffer = b'' # creating a buffer
            while buffer[-2:] != b'\r\n': # pressing 'enter' is the way to send a message
                data = connection.recv(2) # 'downloading' the data sent by the client
                if not data: # if no data is available, then take the next connection
                    break
                else:
                    print(f'I got data: {data}!')
                    buffer = buffer + data
            print(f"All the data is: {buffer}")
            connection.send(buffer) # sending the mesage back to the client
finally:
    server_socket.close() # realeasing the resources