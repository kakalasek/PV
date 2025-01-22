import threading
import socket

class BreakException(Exception):
    pass

class UserThread(threading.Thread):

    def __init__(self, connection, client_inet_address, commands):
        super().__init__()
        self._connection: socket.socket = connection
        self._client_inet_address = client_inet_address
        self._commands: dict = commands
        self._commands['exit'] = self._exit

    def run(self):
        try:
            self._connection.send(b'Hello there\n')
            while True:
                command = self._connection.recv(20).strip()
                command = str(command, 'utf-8')

                if command not in self._commands.keys():
                    self._connection.send(b'This command does not exist\n')
                else:
                    output = self._commands[command]()
                    if output:
                        self._connection.send(output)
                    self._connection.send(b'\n')

        except BreakException as e:
            pass
        except Exception as e:
            print(e)
        finally:
            self._connection.close()
            print("Connection closed")

    def sendMessage(self, message):
        self._connection.send(message)

    def _exit(self):
        raise BreakException