num=int(input("Enter a number:"))
temp=num
def strongno(num):  
    sum=0
    while(num):
        i=1
        fact=1
        rem=num%10
        while(i<=rem):
            fact=fact*i
            i=i+1
        sum=sum+fact
        num=int(num/10)
    return sum
if(strongno(num)==temp):
    print(temp,"is a strong number")
else:
    print(temp,"is not a strong number")