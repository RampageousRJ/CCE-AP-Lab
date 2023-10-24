import socket

def search(nums, key):
    for i in nums:
        if i == key:
            return True
    return False

def split(nums):
    odd,even = [],[]
    for i in nums:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i) 
    return odd,even


if __name__=='__main__':
    sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    sockfd.bind((host,3355))

    sockfd.listen(5)

    while True:
        newsockfd, addr = sockfd.accept()
        print("Got connection from : ", addr)
        newsockfd.send("Send an Integer array : ".encode())
        arr = newsockfd.recv(1024).decode().strip('b\'[]').split(",")
        arr = [int(x) for x in arr]
        while True:
            buff = newsockfd.recv(1024).decode().strip('b\'[]').split(",")
            buff = [int(x) for x in buff]
            option = buff[0]
            if option == 1:
                key = buff[1]
                newsockfd.send(str(search(arr,key)).encode())
            elif option == 2:
                arr=sorted(arr)
                newsockfd.send(str(arr).encode())
            elif option == 3:
                odd,even = split(arr)
                newsockfd.send(str(odd).encode())
                newsockfd.send(str(even).encode())
            elif option == 4:
                newsockfd.close()
                sockfd.close()
                exit()