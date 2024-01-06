import socket
import select

HEADER_LENGTH = 10

host = "127.0.0.1"
port = 8080

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # This modifies the socket to allow us to reuse the address.

s.bind((host,port))
s.listen()
# we'll create a list of sockets for select to keep track of, as well as begin our clients dict:
socket_list=[s]
clients={}
print(f'Listening for connections on {host}:{port}...')

# Handles message receiving
def receive_message(client_socket):
    try:
        message_header = client_socket.recv(HEADER_LENGTH)
        if not len(message_header):
            return False
        message_length = int(message_header.decode('utf-8').strip())
        return {'header': message_header, 'data': client_socket.recv(message_length)}
    
    except:
        return False


while True:
    read_sockets, _, exception_sockets = select.select(socket_list, [], socket_list)
    for notified_socket in read_sockets:
        if notified_socket == s:
            client_socket, client_address = s.accept()
            user = receive_message(client_socket)
            if user is False:
                continue    
            socket_list.append(client_socket)
            print(user)
            clients[client_socket]=user
            print('Accepted new connection from {}:{}, username: {}'.format(*client_address, user['data'].decode('utf-8')))
        else:
            message = receive_message(notified_socket)
            if message is False:
                print('Closed connection from: {}'.format(clients[notified_socket]['data'].decode('utf-8')))
                socket_list.remove(notified_socket)
                del clients[notified_socket]
                continue
            print(message)

            user = clients[notified_socket]
            print(f'Received message from {user["data"].decode("utf-8")}: {message["data"].decode("utf-8")}')
            for client_socket in clients:
                if client_socket != notified_socket:
                    client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])


