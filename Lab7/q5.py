import re
str = input("Enter string: ")
pattern = r"^([a-zA-Z]).*\1$"
if re.match(pattern,str):
    print('True')
else:
    print("False")