import socket

HOST = "127.0.0.1"
PORT = 8080

while True:
    input_data = input()
    input_data_as_bytes = str.encode(input_data)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(input_data_as_bytes)
        data = s.recv(2048)

        print(f'Recieved {data.decode()}')