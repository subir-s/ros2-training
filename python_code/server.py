import socket

def start_server(host='localhost', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f'Server listening on {host}:{port}')

        while True:
            conn, addr = server_socket.accept()
            with conn:
                print(f'Connected by {addr}')
                data = conn.recv(1024)
                if not data:
                    break
                message = data.decode('utf-8')
                print(f'Received message: {message}')
                response = f"Hello, I received the {message}"
                conn.sendall(response.encode('utf-8'))

if __name__ == "__main__":
    start_server()