def findsum(num):
    sum=0
    while num!=0:
        rem=num%10
        num=int(num/10)
        sum+=rem
    return sum
n=int(input('Enter any number: '))
print('Sum of digits of',n,'is:'+str(findsum(n)))