swed={"merry":"god","christmas":"jul","happy":"gott","year":"ar","and":"och","new":"nytt"}
list_eng=[]
i=0
n=int(input("Enter the number of words in your message:"))
while i<n:
    eng=input("Enter the message word by word:")
    list_eng.append(eng)
    i=i+1
for i in list_eng:
    for key,value in swed.items():
        if i==key:
            print(value,end=" ")
quit()
print("Enter valid message")