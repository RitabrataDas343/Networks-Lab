import socket as soc

c = soc.socket()
port = 5000
c.connect(('127.0.0.1', port))
while True:
    send_msg = input("Send message to server : ")
    c.send(send_msg.encode('utf-8'))
    if send_msg.lower() == "bye":
        break
    recv_msg = c.recv(1024).decode('utf-8')
    print(f"Server: {recv_msg}\n")
c.close()
