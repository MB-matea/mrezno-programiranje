# -- coding: utf-8 --
# echo_client.py
import socket

host = socket.gethostname()
port = 12345
client_socket = socket.socket()  # tcp socket

client_socket.connect((host, port))

client_socket.sendall("Tekst koji se salje serveru".encode())

data = client_socket.recv(1024)  # tekst koji je primljen od servera

print(data)
client_socket.close()