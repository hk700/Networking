from socket import socket, AF_INET, SOCK_STREAM
s = socket(AF_INET, SOCK_STREAM)
s.connect(('127.0.0.1', 8888))
s.sendall("comnetsii")
data = s.recv(1024)
print("received", data)
print("The string after binary conversion : " + str(data))
s.close()
