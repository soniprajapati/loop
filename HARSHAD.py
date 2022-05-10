# def harshad(num):
#     sum = 0
#     d= num
#     while d > 0:
#         sum = sum + d % 10
#         d= d // 10
#     if(num % sum == 0):
#         return True
#     else:
#         return False
# low= 1
# upper= 100
# print('The Harshad numbers in the given range',
#       low, 'and', upper, 'are:')
# for i in range(low, upper+1):
#     if(harshad(i)):
#         print(i, end=' ')



for i in range(1,11):
    if i%2==0:
        print(i)
for j in range(1,11):
    if j%2==1:
        print(j)