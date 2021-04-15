# -- coding: utf-8 --
# echo_client.py
import socket
import datetime
from local_machine_info import print_machine_info

print_machine_info()
print(datetime.datetime.now())

host = socket.gethostname()
port = 12345
client_socket = socket.socket()  # tcp socket

client_socket.connect((host, port))

print("Unesite tekst koji zelite poslati: ")
data = input()

client_socket.sendall(data.encode())

data = client_socket.recv(1024)  # tekst koji je primljen od servera

print(data)

client_socket.close()
