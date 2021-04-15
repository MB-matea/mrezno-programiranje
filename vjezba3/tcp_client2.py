# tcp_client.py

import socket

client_socket = socket.socket()
host = socket.gethostname()
port = 9999
 
client_socket.connect((u"216.58.209.196", 80))
print("Socket se uspješno spojio na Google na port = ", 80," i IP adresu = " , u"216.58.209.196")
 
client_socket.close()