L=input()
a=int(input())
M=L.split()
M=list(map(int,M))
M=M[:-1:]
M.sort()
i=0
j=len(M)-1
while i<j:
    if M[i]+M[j]<a:
        i+=1
    elif M[i]+M[j]>a:
        j-=1
    else:
        break
def aab():
    if i==j:
        return None
    if M[i]+M[j]==a:
        return [i,j]
print(aab())