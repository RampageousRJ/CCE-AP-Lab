import sys

try:
    file = open(sys.argv[1],'r')
    otp = open("temp.txt",'w')
    wrap = int(sys.argv[2])
    sentences = file.readlines()
    sentences = [word for x in sentences for word in [x[:wrap:]+"\n",x[wrap::]]]
    otp.writelines(sentences)

except FileNotFoundError:
    pass