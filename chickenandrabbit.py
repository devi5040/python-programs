def change(heads,legs):
    rabbit_count=0
    chicken_count=0
    if legs%2!=0 or legs<heads:
        print("No solution")
    elif legs%4==0 and int(legs/4)==heads:
        print('0:chickens\t',heads,':rabbits')
    elif legs%2==0 and int(legs/2)==heads:
        print(heads,':chickens\t','0:rabbits')
    else:
        rabbit_count=1
        while True:
            legs=legs-4
            chicken_count=int(legs/2)
            if chicken_count+rabbit_count==heads:
                print(chicken_count,':chickens\t',rabbit_count,':rabbits')
                break
            else:
                rabbit_count+=1
a=int(input("Enter the no. of heads: "))
b=int(input("Enter no. of legs: "))
change(a,b)