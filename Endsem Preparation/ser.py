import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),3355))
s.listen(1)
while True:
    ns,addr = s.accept()
    while True:
        val = ns.recv(1024).decode()
        print(val)
        if val=='Stop':
            break
        val = input("Enter text: ")
        ns.send(val.encode())
        if val=='Stop':
            break
    break