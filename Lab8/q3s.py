import socket
sockfd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
sockfd.bind((host,3355))
sockfd.listen(1)
while True:
    newsockfd, addr = sockfd.accept()
    print("\nConnected from", addr)
    while True:
        rstr = newsockfd.recv(1024).decode()
        print(f"Recieved [{rstr}]")
        if rstr=="Stop":
            break
        length = len(rstr)
        rstr = rstr.lower()
        vowel=0
        for char in rstr:
            if char=='a' or char=='e' or char=='i' or char=='o' or char=='u':
                vowel+=1
        if(rstr == rstr[::-1]):
            newsockfd.send((f"String is PALINDROME with length {length} and vowel count {vowel}").encode())
        else:
            newsockfd.send((f"String is NOT PALINDROME with length {length} and vowel count {vowel}").encode())
    print("Disconnecting from",addr)
    newsockfd.close()