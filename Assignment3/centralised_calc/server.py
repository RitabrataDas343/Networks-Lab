import socket as soc

s =  soc.socket()
print("Socket successfully created")

port = 4321
s.bind(('127.0.0.1', port))
print(f"Socket successfully binded to port: {port}")

s.listen(5)
print("Waiting for connection...\n")

c, addr = s.accept()

while True:
    data = c.recv(1024).decode()
    
    if(not data):
        print("Received EXIT from client..")
        break 
    else:
        print(f"Expression Received:{data}\n")

    t = data.split(',')
    operations = t[0]
    num1 = int(t[1])
    num2 = int(t[2])

    if(operations == "add"):
        reply = num1 + num2
    elif(operations == "sub"):
        reply = num1 - num2
    elif (operations == "mul"):
        reply = num1 * num2
    elif (operations == "div"):
        reply = num1 / num2
    else:
        reply = 0

    c.send(str(reply).encode())

c.close()

    
