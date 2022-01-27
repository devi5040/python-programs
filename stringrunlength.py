def encode(message):
    list=[]
    count=0
    base=message[0]
    for i in message:
        if i==base:
            count+=1
        else:
            list.append(str(count)+base)
            base=i
            count=1
    list.append(str(count)+base)
    name=''
    for i in list:
        name=name+i
    return name
code=input("Enter the message: ")
encoded_message=encode(code)
print('coded message is:',encoded_message)