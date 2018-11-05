even=0
odd=0
for x in range(1,11):
    no=int(input("enter the number"))
    if  no%2==0:
        even+=1
    else:
        odd+=1
print("no of even numbers:",even)
print("no of odd numbers:",odd)