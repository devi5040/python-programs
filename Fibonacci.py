n=int(input("Enter a number:"))
num_list=[]
def generate_fibonacci(num):
    i=2
    num1=0
    num2=1
    if num==1:
        return num_list.append(num1)
    else:
        num_list.append(num1)
        num_list.append(num2)
        while i<n:
            temp=num1
            num1=num2
            num2=temp+num2
            num_list.append(num2)
            i+=1
    return num_list
print(generate_fibonacci(n))
