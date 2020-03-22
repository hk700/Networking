from socket import socket, AF_INET, SOCK_DGRAM
import cleanup
from packet import *
from printer import *

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('192.168.1.1', 0))
server = ('192.168.2.1', 8888)
s.sendto("comnetsii", server)
data, addr = s.recvfrom(1024)
print("received", data, "from", addr)
s.close()