num=int(input("Enter a number:"))
n=int(input("Enter the positions to be shifted:"))
def binshift(x,n):
    shift=x>>n
    return shift
print("After shifting=",binshift(num,n))