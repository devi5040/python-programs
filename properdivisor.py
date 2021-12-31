num=int(input("Enter a number:"))
list_num=[]
def proper_divisor(n):
    for i in range(1,n+1):
        if n%i==0:
            list_num.append(i)
    return list_num
print("Proper divisors are:",proper_divisor(num))
