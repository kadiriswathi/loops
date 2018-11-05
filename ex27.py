big1=0
big2=0
for x in range(1,11):
    no=int(input("enter the number"))
    if big1<no:
        if big2<no:
            big2=big1
            big1=no
print(big1,"is a first big number")
print(big2,"is a second big number")