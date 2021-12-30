n=int(input("Enter the number of passengers:"))
k=0
list_src=[]
list_dest=[]
list_num=[]
while k<n:
    source=input("Enter the source city:")
    list_src.append(source[0:3])
    destin=input("Enter the destination:")
    list_dest.append(destin[0:3])
    k+=1
for i in range(101,1000):
    count=0
    if count<n:
        list_num.append(i)
        i=i+1
        count=count+1
for j in range(0,n):
    print("AL1"+list_src[j]+list_dest[j]+str(list_num[j]))