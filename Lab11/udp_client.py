import socket
from config import HOST, PORT

print('\n=== TCP ===')
print(' > CLIENT')


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.connect((HOST, PORT))

    filename = input('\nEnter file to request from server: ')

    sock.sendall(bytes(filename, 'utf-8'))
    print(f'\nSent: {filename}')

    data = sock.recv(1024).decode('utf-8')
    print(f'\nReceived: {data}')
    print()
