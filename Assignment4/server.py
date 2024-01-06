import socket as soc
import threading as th

def handle_client(client, address):
    flag = True
    while flag:
        recv_msg = client.recv(1024).decode('utf-8')
        print(f"Client {address} : {recv_msg}\n")
        if(recv_msg.lower() == 'bye'):
            flag = False
            s.close()
            break

        send_msg = input(f"Send message to client: ")
        client.send(send_msg.encode('utf-8'))
        
    print(f"Client {address} is disconnected")
    client.close()

s = soc.socket()
print("Socket successfully created")

port = 5000
s.bind(('127.0.0.1', port))
print(f"Server listening on port {port}")

s.listen(5)
print("Waiting for connection...\n")

while True:
    c, addr = s.accept()
    print(f"Connected to address: {addr}")
    thread = th.Thread(target=handle_client, args=(c, addr))
    thread.start()
