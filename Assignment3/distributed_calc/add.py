import socket as soc

while True:
    s =  soc.socket()
    print("Socket successfully created")

    port = 2000
    s.bind(('127.0.0.1', port))
    print(f"Socket successfully binded to port: {port}")

    s.listen(5)
    print("Waiting for connection...\n")

    c, addr = s.accept()

    while True:
        data = c.recv(1024).decode('ascii')

        if(not data):
            break
        
        print(f"Expression Received:{data}\n")

        t = data.split(',')
        operations = t[0]
        num1 = int(t[1])
        num2 = int(t[2])

        reply = num1+num2
        print(f"Result: {reply}\n")
        c.send(str(reply).encode('ascii'))
    c.close()




    
