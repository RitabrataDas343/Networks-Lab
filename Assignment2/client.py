import socket as soc

c = soc.socket()
port = 4321
c.connect(('127.0.0.1', port))

while True:
    msg = input("Enter message from client: ")
    c.send(msg.encode('ascii'))
    if msg == "!DISCONNECT":
        break
    else:
        msg = c.recv(256).decode('ascii')
        print(f"\nMessage Received: {msg}\n")
c.close()