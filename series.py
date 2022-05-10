#Write a program to print the following series till n terms.
#2 , 22 , 222 , 2222 _ _ _ _ _ n terms

n=int(input("enter number:"))
i=0
while i<=n:
    j=0
    while j<=i:
        num=i%10
        i=i//i
        j+=1
    if num==2:
        print(num,end="")
    i+=1
    
#under constraction