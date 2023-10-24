import socket
sockfd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
sockfd.connect((host,3355))
while True:
    string = input("Enter the String: ")
    sockfd.send(string.encode())
    if string=="Stop":
        break
    print(sockfd.recv(1024).decode())
    print()
sockfd.close()