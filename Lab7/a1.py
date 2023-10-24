try:
    file = open('inp.txt','r')
    for line in file:
        line=line.strip('\n')
        print(line[::-1])
except FileNotFoundError:
    print("File does not exist") 