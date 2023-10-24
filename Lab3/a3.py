def inner():
    print("Inner Function")
    
def outer():
    print("Outer Start")
    inner()
    print("Outer End")

if __name__=='__main__':
    outer()