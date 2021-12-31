i=0
y=int(input("Enter a year:"))
list_y=[]
if(y%4==0 and y%100!=0 or y%400==0):
    list_y.append(y)
    i=i+1
    while(i<15):
        year=y+(4*i)
        i=i+1
        list_y.append(year)
if i!=0:
    print(list_y)
else:
    print("Not a leap year")