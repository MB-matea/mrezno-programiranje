# -- coding: utf-8 --
# echo_server.py
import socket
import datetime
from local_machine_info import print_machine_info

print_machine_info()
print(datetime.datetime.now())

host = socket.gethostname()
port = 12345
echo_server = socket.socket()  # tcp socket

echo_server.bind((host, port))
echo_server.listen(5)

while True:
    conn, addr = echo_server.accept()
    print("Spojen: ", addr)
    data = conn.recv(1024)  # prihvaćanje podataka od klijenta
    if data == b"matea_beslic":
        data2 = "Unos nije podrzan"
        conn.sendall(data2.encode())
        break
    else:
        conn.sendall(data)  # vrati primljene podatke klijentu

conn.close()
