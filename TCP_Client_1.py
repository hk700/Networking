from socket import socket, AF_INET, SOCK_STREAM
s = socket(AF_INET, SOCK_STREAM)
s.connect(('10.0.2.15', 8888))
s.sendall("110001111011111101101110111011001011110100111001111010011101001")
data = s.recv(1024)
print("received", data)

print("The Binary value after string conversion is:",  data) 
s.close()
