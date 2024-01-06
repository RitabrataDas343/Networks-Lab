import socket as soc

s =  soc.socket()
print("Socket successfully created")

port = 4321
s.bind(('127.0.0.1', port))
print(f"Socket successfully binded to port: {port}")

s.listen(5)
print("FTP is ready...\n")

while True:
    conn, addr = s.accept()
    print(f"Client {addr} is connected.")

    filename = conn.recv(1024).decode("utf-8")
    if(not filename):
        break
    
    print(f"\nReceiving the filename.....")

    file = open(filename, "w")
    conn.send(f"Filename received: {filename}".encode("utf-8"))

    data = conn.recv(1024).decode("utf-8")
    print(f"Receiving the file data from {filename}.....")
    file.write(data)
    conn.send("File data received.\n".encode("utf-8"))

    file.close()
    conn.close()
    print(f"\nClient {addr} is disconnected.\n")

print("\nClosing the server...")
s.close()
