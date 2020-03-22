from socket import socket, AF_INET, SOCK_STREAM

s = socket(AF_INET, SOCK_STREAM)
s.bind(('10.0.2.15', 8888))
s.listen(1)
conn, addr = s.accept()

def BinaryToDecimal(binary):  
         
    binary1 = binary  
    decimal, i, n = 0, 0, 0
    while(binary != 0):  
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)  
        binary = binary//10
        i += 1
    return (decimal) 
str_data =' '
while 1:
    data = conn.recv(1024)
    if not data: break

    for i in range(0, len(data), 7): 
      
        temp_data = int(data[i:i + 7]) 
       
        decimal_data = BinaryToDecimal(temp_data) 
       
        str_data = str_data + chr(decimal_data)

    print("Connection from", addr)
    print("The binary value is:", data) 
    conn.sendall(str_data)
    
conn.close()
