import socket
host=socket.gethostname
target_host=socket.gethostbyname(host)
target_port=80

cliente=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cliente.connect((target_host,target_port))
cliente.send("GET / HTTP/1.1\r\nHost:google.com\r\n\r\n")
resp=cliente.recv(4096)
print(resp)