import socket
import sys

def send_message(host='localhost', port=65432, message='Hello, World!'):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        client_socket.sendall(message.encode('utf-8'))
        data = client_socket.recv(1024)
        print('Received', repr(data.decode('utf-8')))

if __name__ == "__main__":
    # Check if a message argument is provided
    if len(sys.argv) > 1:
        message = sys.argv[1]
    else:
        message = 'Hello, World!'
    
    send_message(message=message)