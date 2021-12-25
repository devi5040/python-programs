num1=int(input("Enter a number:"))
num2=int(input("Enter anoter number:"))

def amicable(num1,num2):
    sum1=0
    sum2=0

    for i in range(1,num1+1):
        if num1%i==0:
            sum1=sum1+i
        else:
            pass
    for j in range(1,num2+1):
        if num2%j==0:
            sum2=sum2+j
        else:
            pass
    if sum1==sum2:
        return 1
    else:
        return 0
if amicable(num1,num2): 
    print(num1,"&",num2,"are amicable numbers")
else:
    print(num1,"&",num2,"are not amicable numbers")
