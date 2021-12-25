num=int(input("Enter an integer number:"))
def palindrome(n):
    rem=0
    rev=0
    while n!=0:
        rem=n%10
        n=int(n/10)
        rev=rev*10+rem
    return rev
if palindrome(num)==num:
    print(num,"is a palindrome number")
else:
    print(num,"is not a palindrome")