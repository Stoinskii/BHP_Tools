import socket
import threading

IP = '0.0.0.0'
PORT = 9998

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    server.listen(5)
    print(f'[*] Litening on {IP}:{PORT}')

    while True:
        client, address = server.accept()
        print(f'[*] Connection with {address[0]}:{address[1]}')
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f'[*] Received: {request.decode("UTF-8")}')
        sock.send(b'ACKKK')

if __name__=='__main__':
    main()

# To test if the TCP Server is working use TCP Client