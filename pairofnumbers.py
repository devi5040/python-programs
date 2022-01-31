m=int(input("Enter the no. of elements in list: "))

list_num=[]
for i in range(m):
    item=input("Enter the item: ")
    list_num.append(i)
n=int(input("Enter the value of n: "))
def find_pairs_of_numbers(num_list,n):
    count=0
    for i in num_list:
        for j in num_list:
            if i<=n and j<=n:
                if i+j==n and i!=j:
                    count+=1
    count=int(count/2)
    return count
print(find_pairs_of_numbers(list_num,n))
