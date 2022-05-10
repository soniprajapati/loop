i=int(input("enter number:"))
b=i
sum=0
while i>0:
    sum=(sum*10)+(i%10)
    a=sum
    i=i//10
if a==b:
    print(b,"its a palindrome number")
else:
    print(b,"its not a palindrome")