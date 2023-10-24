# READ FROM FILE  
try:
    f = open('test.txt','rt')
    print(f.read())
    f.close()  
except FileNotFoundError:
    print("File Does Not Exist")
    
# WRITE INTO FILE
# f=open('test.txt', 'w')
# f.write("OVERWRITE FILE")
# f.close()

# APPEND INTO FILE
# f=open('test.txt','a')
# f.write("\tAPPEND VALUE")
# f.close()