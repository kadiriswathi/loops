postive=0
negtive=0
for x in range(1,11):
    num=int(input("enter the number:"))
    if num>=1:
        postive+=1
    else:
        negtive+=1
print("no of postive numbers:",postive)
print("no of negative numbers:",negtive)