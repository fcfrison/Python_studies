'''
Creating a server that echoes back messages sent by clients. 
This application is highly inefficient, because it demands a 
lot of cpu resources. 

The code below was created by Matthew Fowler in the book 'Python 
Concurrency with asyncio-Manning Publications (2022)'. 
'''
import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_address = ('127.0.0.1', 8000)
server_socket.bind(server_address)
server_socket.listen()
server_socket.setblocking(False)
connections = []

try:
    while True:
        try:
            connection, client_address = server_socket.accept() # Given that the server socket is non-blocking, if no connection
                                                                # has been established, then an error is raised
            connection.setblocking(False)
            print(f'I got a connection from {client_address}!')
            connections.append(connection)
        except BlockingIOError:
            pass
        for connection in connections: # if a connection has been created, then iterates the list.
            try:
                buffer = b''
                while buffer[-2:] != b'\r\n':
                    data = connection.recv(2) # If no message has been loaded, then an error is raised.
                    if not data: 
                        break
                    else:
                        print(f'I got data: {data}!')
                        buffer = buffer + data
                print(f"All the data is: {buffer}")
                connection.send(buffer)
            except BlockingIOError:
                pass
finally:
    server_socket.close()


