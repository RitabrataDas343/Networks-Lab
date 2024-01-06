import socket as soc
import threading as th

def handle_client(c, addr):
    connected = True
    while connected:
        msg = c.recv(256).decode()
        print(f"Address: {addr}\nMessage Received: {msg}\n")
        if (msg == "!DISCONNECT"):
            connected = False
        message = input("Enter message from server: ")
        c.send(message.encode('ascii'))
    c.close()

s =  soc.socket()
print("Socket successfully created")

port = 4321
s.bind(('127.0.0.1', port))
print(f"Socket successfully binded to {port}")

s.listen(5)
print("Waiting for connection")

while True:
    c, addr = s.accept()
    print("Got connection from", addr)
    t = th.Thread(target = handle_client, args=(c, addr))
    t.start()
    print(f"No. of active connection = {th.activeCount()-1}","\n")
