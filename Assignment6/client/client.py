import socket as soc
import sys
import os

s = soc.socket()
port = 4321
s.connect(('127.0.0.1', port))

op = input("Enter the operation ('DOWNLOAD'/'UPLOAD'/'QUIT'): ")
s.send(op.encode('ascii'))

if op.lower() == "quit":
    print("Exiting client....")
    sys.exit()

elif op.lower() == "download":
    print('Files on the server: ')
    files = s.recv(1024).decode('ascii')
    print(files)
    file_name = input("Enter the file to download: ")
    s.send(file_name.encode())
    with open(file_name, 'wb') as f:
        data = s.recv(1024)
        while data:
            f.write(data)
            data = s.recv(1024)
    print('File Downloaded!!!!\nBye..')
    s.close()

elif op.lower() == "upload":
    print('Files on the client: ')
    file_names = ""
    with os.scandir('./') as files:
        for file in files:
            file_names = file_names + str(file.name) + '\n'
    print(file_names)
    file_name = input("Enter the file to upload: ")
    s.send(file_name.encode('ascii'))
    try:
        with open(file_name, 'rb') as f:
            data = f.read()
            s.sendall(data)
    except FileNotFoundError:
        print('File Not Found')
    print('File Uploaded!!!!\nBye..')
    s.close()