# -- coding: utf-8 --
# echo_server.py
import socket

host = socket.gethostname()
port = 12345
echo_server = socket.socket()  # tcp socket

echo_server.bind((host, port))
echo_server.listen(5)

print("Cekam klijenta!")
conn, addr = echo_server.accept()  # prihvaćanje konekcije kada se klijent spoji

print("Spojen: ", addr)

while True:
    data = conn.recv(1024)  # prihvaćanje podataka od klijenta
    if not data:  # ako nema podataka, izađi
        break
    conn.sendall(data)  # vrati primljene podatke klijentu

conn.close()
