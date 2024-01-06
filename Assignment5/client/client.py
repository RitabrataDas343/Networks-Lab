import socket as soc
import os

c = soc.socket()
port = 4321
c.connect(('127.0.0.1', port))

files = os.listdir('./')
print("The files that can be send via FTP are: ")
count = 1
for entry in files:
    if not entry.endswith('.py'):
        print(str(count) + '. ' + entry)
        count = count + 1

filename = input("Enter the name of the file to send (Enter \'bye\' to exit): ")

if(filename != 'bye'):
    file = open(filename, "r")
    data = file.read()

    c.send(filename.encode("utf-8"))
    msg = c.recv(1024).decode("utf-8")
    print(f"Sending filename to server.\nMessage from Server: {msg}")

    c.send(data.encode("utf-8"))
    msg = c.recv(1024).decode("utf-8")
    print(f"Message from Server: {msg}")

    file.close()

print("\nExiting client...")
c.close()
