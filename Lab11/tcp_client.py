import socket
from config import HOST, PORT

print('\n=== TCP ===')
print(' > CLIENT')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))

    filename = input('\nEnter file name: ')

    sock.sendall(bytes(filename, 'utf-8'))
    print(f'\nSent: {filename}')

    data = sock.recv(1024)
    contents = data.decode('utf-8')
    print(f'\nReceived: {contents}')
    print()
