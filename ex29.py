no=int(input("enter the number"))
rev=0
while no!=0:
    rem=no%10
    no=no//10
    rev=rev*10+rem
print("reverse number is:",rev)



