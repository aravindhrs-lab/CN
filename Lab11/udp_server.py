import socket
from config import HOST, PORT


print('\n=== UDP ===')
print(' > SERVER')

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.bind((HOST, PORT))

    data, addr = sock.recvfrom(1024)

    filename = data.decode('utf-8')
    print(f'\nReceived Filename: {filename} From: {addr}')

    try:
        with open(filename, 'r') as f:
            data = f.read()
        data = bytes(data, 'utf-8')
    except:
        data = bytes(f'File {filename} not found', 'utf-8')

    sock.sendto(data, addr)
    print(f'\nSent: {data} To: {addr}')
    print()
