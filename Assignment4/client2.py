import socket
import threading

class ReceiveThread(threading.Thread):
    def __init__(self, server_socket, username):
        super().__init__()
        self.server_socket = server_socket
        self.username = username

    def run(self):
        while True:
            message = self.server_socket.recv(1024).decode()
            if not message:
                print("Connection closed by server")
                break
            sender, message = message.split(">", 1)
            if sender != self.username:
                print(f"\n{sender} -> {message}\n")

HOST = "localhost"
PORT = 8000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
print(f"Connected to {HOST}:{PORT}")

username = input("Enter your username: ")
print(f"Logged in as {username}")
receive_thread = ReceiveThread(client_socket, username)
receive_thread.start()

while True:
    message = input(f"{username} -> ")
    if message.lower() == "quit":
        break
    client_socket.sendall(f"{username} -> {message}".encode())

print("Closing connection")
client_socket.close()
