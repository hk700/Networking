from socket import socket, AF_INET, SOCK_STREAM

s = socket(AF_INET, SOCK_STREAM)
s.bind(('127.0.0.1', 8888))
s.listen(1)
conn, addr = s.accept()

while 1:
    data = conn.recv(1024)
    if not data: break
    print("Connection from", addr)
    print("The original string is : " + str(data))
    res = ''.join(format(ord(i), 'b') for i in data)
    conn.sendall(res)
    
conn.close()
