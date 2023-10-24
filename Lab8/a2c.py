import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
s.connect((host,3355))

arr = []
nums = int(input("Enter the number of elements : "))
print(s.recv(1024).decode().strip('b\''))
for i in range(nums):
    arr.append(int(input("Enter number : ")))
s.send(str(arr).encode())
while True:
    ch = int(input("MENU\n1.Search\n2.Sort\n3.Split\n4.Exit\nEnter choice: "))
    if ch == 1:
        key = int(input("Enter key: "))
        buff = [ch,key]
        s.send(str(buff).encode())
        print(s.recv(1024).decode().strip('b\''))
    elif ch == 2:
        buff = [ch]
        s.send(str(buff).encode())
        print(s.recv(1024).decode().strip('b\''))
    elif ch == 3:
        buff = [ch]
        s.send(str(buff).encode())
        print(s.recv(1024).decode().strip('b\''))
        print(s.recv(1024).decode().strip('b\''))
    elif ch == 4:
        buff = [ch]
        s.send(str(buff).encode())
        s.close()
        exit()