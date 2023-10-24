try:
    num1 = int(input("Enter Num1: "))
except ValueError:
    print("Not real numbered")
    exit()
op = input("Enter operator: ")
try:
    num2 = int(input("Enter Num2: "))
except ValueError:
    print("Not real numbered")
    exit()

if op=="+":
    print(num1+num2)
elif op=="-":
    try:
        if num1<num2:
            raise InterruptedError
    except InterruptedError:
        print("Num1 smaller")
        exit()
    print(num1-num2)
elif op=="*":
    print(num1*num2)
elif op=="/":
    try:
        print(num1/num2)
    except ZeroDivisionError:
        print("Trying to divide by zero")
        exit()
else:
    print("Incorrect Operator")