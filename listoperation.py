n=int(input("Enter the number of elements:"))
list=[]
for j in range(0,n):
    item=int(input("enter element "))
    list.append(item)
count=0
i=0
while i<n-1:
    if list[i]==list[i+1]:
        count=count+1
    else:
        i=i+1
        continue
    i=i+1
if count==0:
    print("No adjascent elements")
else:
    print(count,"Adjascent elements are present")