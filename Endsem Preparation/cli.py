import socket
s = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM,proto=0)
s.connect((socket.gethostname(),3355))
while True:
    val = input("Enter text: ")
    s.send(val.encode())
    if val=='Stop':
        break
    val = s.recv(1024).decode()
    print(val)
    if val=='Stop':
        break