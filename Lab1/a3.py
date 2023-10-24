s=str(input('Enter string: '))
valid="0123456789ABCDEF"
flag=True
for i in s:
    if i not in valid:
        flag=False
        print('Not a valid hexadecimal')
        break
if flag:
    print('Valid hexadecimal')