import socket
from config import HOST, PORT

print('\n=== TCP ===')
print(' > SERVER')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((HOST, PORT))
    sock.listen(1)
    conn, addr = sock.accept()

    with conn:
        print(f'\nConnected by: {addr}')
        while True:
            data = conn.recv(1024)
            if not data:
                break

            filename = data.decode('utf-8')
            print(f'\nReceived Filename: {filename}')

            try:
                with open(filename, 'r') as f:
                    data = f.read()
                data = bytes(data, 'utf-8')
            except:
                data = bytes(f'File {filename} not found', 'utf-8')

            conn.sendall(data)
            print(f'\nSent: {data}')
            print()
