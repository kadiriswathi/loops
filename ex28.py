prime=0
for x in range(1,11):
    num=int(input("enter the number"))
for y in range(2,num):
    if num%y==0:
        print(end=" ")
        break
    else:
        prime+=1

print("no of prime numbers:",prime)