import socket
from MyServer.UserConnection import UserThread
from MyServer.Commands import returnCitat, returnDatum

class ServerConnection():
    
    def __init__(self, host, port):
        server_inet_address = (host, port)
        self._server_socket = socket.socket()
        self._server_socket.bind(server_inet_address)
        self._userThreadPool = []
        self._commands = {'help': self._help,
                          'shutdown': self._broadcast,
                          'citat': returnCitat,
                          'datum': returnDatum}

    def startListening(self):
        try:
            self._server_socket.listen()

            while True:
                connection, client_inet_address = self._server_socket.accept()
                new_thread = UserThread(connection, client_inet_address, self._commands)
                self._userThreadPool.append(new_thread)
                new_thread.start()

        except Exception as e:
            print(e)
        finally:
            self._shutdown()

    def _help(self):
        help = self._commands.keys()
        return ", ".join(f'{k}' for k in help).encode('utf-8')
    
    def _broadcast(self):
        for t in self._userThreadPool:
            t.sendMessage(b'Broadcast message')

    def _shutdown(self):
        self._server_socket.close()
        print("Server Exit")

        for t in self._userThreadPool:
            t._exit()