import socket
import threading

class ServerThread(threading.Thread):
    def __init__(self, server_socket):
        super().__init__()
        self.server_socket = server_socket
        self.client_sockets = []

    def run(self):
        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"Connection established with {client_address}")
            self.client_sockets.append(client_socket)
            client_handler_thread = ClientHandlerThread(client_socket, self.client_sockets)
            client_handler_thread.start()

class ClientHandlerThread(threading.Thread):
    def __init__(self, client_socket, client_sockets):
        super().__init__()
        self.client_socket = client_socket
        self.client_sockets = client_sockets

    def run(self):
        while True:
            message = self.client_socket.recv(1024).decode()
            if not message:
                self.client_socket.close()
                self.client_sockets.remove(self.client_socket)
                print(f"Connection closed with {self.client_socket.getpeername()}")
                break
            print(f"Received message: {message}")
            for client_socket in self.client_sockets:
                if client_socket != self.client_socket:
                    client_socket.sendall(message.encode())

if __name__ == "__main__":
    HOST = "localhost"
    PORT = 8000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print(f"'\033[31mServer listening on {HOST}:{PORT}")
    server_thread = ServerThread(server_socket)
    server_thread.start()
