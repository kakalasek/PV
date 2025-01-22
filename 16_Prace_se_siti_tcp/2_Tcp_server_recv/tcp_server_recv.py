import socket

try:

    host = "127.0.0.1"
    port = 65532

    server_inet_address = (host, port)

    server_socket = socket.socket()
    server_socket.bind(server_inet_address)
    server_socket.listen()
    while True:
        try:
            connection, client_inet_address = server_socket.accept()
            connection.send(b'Hello there\n')
            while True:
                something = connection.recv(20)
                if something.strip() == b'end':
                    connection.send(b'Quitting\n')
                    break
                connection.send(something)
        except Exception as e:
            print(e)
        finally:
            connection.close()

except Exception as e:
    print(e)
finally:
    server_socket.close()
    print("Server is closed")