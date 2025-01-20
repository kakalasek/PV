import socket


try:
    host = "127.0.0.1"
    port = 65533

    server_inet_address = (host, port)

    server_socket = socket.socket()
    server_socket.bind(server_inet_address)
    server_socket.listen()
    print("Server start on " + str(server_inet_address[0]) + ":" + str(server_inet_address[1]))

    connection, client_inet_address = server_socket.accept()
    print("Client connection accepted from " + str(client_inet_address[0]) + ":" + str(client_inet_address[1]))

    message = "Hello there\n"
    message = bytes(message, "utf-8")
    print("Sending bytes:")

    for byte in message:
        print(bin(byte))

    connection.send(message)


except Exception as e:
    print(e)
finally:
    server_socket.close()
    print("Server is closed")

    connection.close()
    print("Client connection closed")