for i,value in enumerate(['a','b','c']):
    print(i,value)

for x,y in [(1,3),(1,4),(3,5)]:
    print(x,y,end='7  ')

a=list(range(2,6))
print(a)

b=[x*x for x in range(5,8) if x%2 == 0]
print(b)

a=[m+n for m in 'abc'for n in 'XYZ']
print(a)

import os
o=[d  for d in os.listdir('.')]
print(o)

L1=['Hello','World',18,'Apple',None]
L2=[]
for x in L1:
    if isinstance(x,str)== 1:
        L2.append(x)
L2=[s.lower() for s in L2]
print(L2)