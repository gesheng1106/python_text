a=int(input())
b=int(input())
x=a+1
k=0
def isushu(a):
    j=0
    for i in range(2,a) :
        if a%i==0 :
           j=1
    if j==1:
        return False
    else:
        return True
def reverseInt(num):
    result = 0
    while num != 0:
        result = result * 10 + num % 10
        num = int(num/10)
    return result
L = []
while x<b:
    if isushu(x) and isushu(reverseInt(x)):
        L.append(x)
        k+=1
    x+=1
if k==0 :
    print('no exit',end='')
else:
    print(L,end='')


