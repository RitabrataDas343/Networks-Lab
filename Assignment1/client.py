import socket as soc

c = soc.socket()
port = 4321
c.connect(('127.0.0.1', port))
print (c.recv(1024).decode())
c.close()