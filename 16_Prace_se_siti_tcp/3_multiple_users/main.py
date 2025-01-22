from MyServer.ServerConnection import ServerConnection

if __name__ == '__main__':
    conn = ServerConnection('127.0.0.1', 65532)
    conn.startListening()