import socket as soc
import os

s =  soc.socket()
print("Socket successfully created")

port = 4321
s.bind(('127.0.0.1', port))
print(f"Socket successfully binded to port: {port}")

s.listen(5)
print("FTP is ready...\n")

flag = True
while flag:
    connection, address = s.accept()
    msg = connection.recv(1024).decode('ascii')
    print(f"The operation is: {msg}\n")

    if msg.lower() == 'quit':
        flag = False
        connection.close()

    elif msg.lower() == "download":
        file_name = ""
        with os.scandir('./') as files:
            for file in files:
                file_name = file_name +  str(file.name) + '\n'
            connection.send(file_name.encode('ascii'))
        file_name = connection.recv(1024).decode('ascii')
        print(f"The name of the file to be downloaded is: {file_name}\n")
        try:
            with open(file_name, 'rb') as f:
                data = f.read()
                connection.sendall(data)
        except FileNotFoundError:
            print('File Not Found')
        connection.close()

    elif msg.lower() == "upload":
        file_name = connection.recv(1024).decode('ascii')
        print(f"The name of the file to be downloaded is: {file_name}\n")
        with open(file_name, 'wb') as f:
            data = connection.recv(1024)
            while data:
                f.write(data)
                data = connection.recv(1024)
            f.close()
            connection.send('Received'.encode('ascii'))
        connection.close()

print("\nClosing the server...")       
connection.close()