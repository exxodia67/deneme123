import socket

host = 'localhost'  # değiştirilebilir
port = 12345  # soket port numarası

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

message = 'Hello Pico!'
s.sendall(message.encode())

s.close()
