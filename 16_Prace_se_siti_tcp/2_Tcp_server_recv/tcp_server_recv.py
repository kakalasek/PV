import socket
import random
from datetime import date

class BreakException(Exception):
    pass

class StopException(Exception):
    pass

def returnCitat(connection: socket.socket):
    citaty = ["Nahodny citat 1", "Nahodny citat 2", "Nahodny citat 3"]
    connection.send(random.choice(citaty).encode("utf-8"))

def returnDatum(connection: socket.socket):
    today = date.today()
    connection.send(today.strftime(f'%Y-%m-%d').encode('utf-8'))

def returnHelp(connection: socket.socket):
    help = commands.keys()
    for cmd in help:
        connection.send(cmd.encode('utf-8') + b'\n')

def handleExit(connection: socket.socket):
    raise BreakException

def handleShutdown(connection: socket.socket):
    raise StopException

try:

    nextConnection = True
    host = "127.0.0.1"
    port = 65533
    commands = {'citat': returnCitat,
                'datum': returnDatum,
                'help': returnHelp,
                'exit': handleExit,
                'shutdown': handleShutdown}

    server_inet_address = (host, port)

    server_socket = socket.socket()
    server_socket.bind(server_inet_address)
    server_socket.listen()

    while True:
        try:
            connection, client_inet_address = server_socket.accept()
            nextConnection = False
            connection.send(b'Hello there\n')
            while not nextConnection:
                command = connection.recv(20).strip()
                command = str(command, 'utf-8')

                if command not in commands.keys():
                    connection.send(b'This command does not exist\n')
                else:
                    commands[command](connection)
                    connection.send(b'\n')

        except BreakException as e:
            nextConnection = True
        except Exception as e:
            raise e
        finally:
            connection.close()
            print("Connection closed")

except StopException as e:
    pass 
except Exception as e:
    print(e)
finally:
    server_socket.close()
    print("Server is closed")