import socket as soc

s =  soc.socket()
print("Socket successfully created")

port = 4321
s.bind(('127.0.0.1', port))
print(f"Socket successfully binded to port: {port}")

s.listen(5)
print("Waiting for connection...\n")

message = 'Server is connected.'

while True:
    c, addr = s.accept()
    print("Got connection from: ", addr)
    c.send(message.encode())
    c.close()
    break
