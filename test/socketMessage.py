import socket
import time
import sys

TCP_IP = '10.0.0.3'
TCP_PORT = 8900

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
s.connect((TCP_IP, TCP_PORT))

while True:
    msg = "test filebeat tcp message send."
    s.send(msg.encode())
    print(msg)
    time.sleep(1)
    data = s.recv(1024)
    print(data.decode())