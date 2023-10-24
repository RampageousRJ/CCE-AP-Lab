import functools
@functools.lru_cache(maxsize=3)
def expensive_calculation(n):
    print("Value for",n,end=": ")
    return n * 2

while(True):
    n=int(input('Enter value(-1 to exit): '))
    if n==-1:
        break
    print(expensive_calculation(n))
