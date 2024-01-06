import socket as soc

c = soc.socket()
port = 4321
c.connect(('127.0.0.1', port))

while True:
    print("1.ADD 2.SUB 3.MUL 4.DIV 5.EXIT\n")
    select = input("Select the operation (1-5): ")

    if(int(select) == 5):
        break

    x = input("Enter X: ")
    y = input("Enter Y: ")

    s = ""

    if int(select) == 1:
        s += "add" + "," + x + "," + y
    elif int(select) == 2:
        s += "sub" + "," + x + "," + y
    elif int(select) == 3:
        s += "mul" + "," + x + "," + y
    elif int(select) == 4:
        s += "div" + "," + x + "," + y

    c.send(s.encode('ascii'))

    ans = c.recv(1024).decode('ascii')
    print(f"\nAnswer: {ans}\n")
c.close()
