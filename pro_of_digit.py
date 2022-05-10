i=int(input("emter number:"))
sum=1
while i>0:
    sum=sum*(i%10)
    i=i//10
print(sum)