import string
def countCase(s):
    cu,cl=0,0
    for i in s:
        if(str(i).isupper()):
            cu+=1
        else:
            cl+=1
    return (cu,cl)

s=input("Enter string: ")
tup = countCase(s)
print("Number of uppercase: ",tup[0])
print("Number of lowercase: ",tup[1])