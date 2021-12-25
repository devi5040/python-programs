n=int(input("Enter an integer number:"))
def factorial(num):
    if num==0:
        return 1
    else:
        return (num*factorial(num-1))
print(n,"!=",factorial(n))