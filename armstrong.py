i=int(input("enter number:"))
a=i
sum=0
while i>0:
    sum=sum+(i%10)**3
    num=sum
    i=i//10
if num==a:
    print(a,"its an armstrong number")
else:
    print(a,"its not an armastrong number")
