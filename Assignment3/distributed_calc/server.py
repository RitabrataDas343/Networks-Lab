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
    data = c.recv(1024).decode('ascii')
    
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
        s1 = soc.socket()
        s1.connect(('127.0.0.1', 2000))
        s1.send(str(data).encode('ascii'))
        result = s1.recv(1024).decode('ascii')
        print(f"Result: {result}\n")
        s1.close()
    elif(operations == "sub"):
        s2 = soc.socket()
        s2.connect(('127.0.0.1', 3000))
        s2.send(str(data).encode('ascii'))
        result = s2.recv(1024).decode('ascii')
        print(f"Result: {result}\n")
        s2.close()
    elif (operations == "mul"):
        s3 = soc.socket()
        s3.connect(('127.0.0.1', 4000))
        s3.send(str(data).encode('ascii'))
        result = s3.recv(1024).decode('ascii')
        print(f"Result: {result}\n")
        s3.close()
    elif (operations == "div"):
        s4 = soc.socket()
        s4.connect(('127.0.0.1', 5000))
        s4.send(str(data).encode('ascii'))
        result = s4.recv(1024).decode('ascii')
        print(f"Result: {result}\n")
        s4.close()
    else:
        result = 0

    c.send(str(result).encode('ascii'))
c.close()


    
