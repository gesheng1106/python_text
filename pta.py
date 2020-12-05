L = eval(input())
M = []
N = []
i = 0
j = 0
# print(L)
for x in L:
    # print(x)
    M.append(x[0])
    N.append(x[1])
for i in range(len(M)):
    for  j in range(len(N)-1):
        j+=1
        if M[i] > M[j] and N[j] >N[i] and i<j:
           L.pop(i)
           L.insert(i,[0,0])
        elif N[j] > M[i] and M[j] <N[i] and i<j:
           L.pop(i)
           L.pop(j-1)
           L.insert(i,[M[j],N[i]])
           L.insert(j,[0,0])
    i+=1
L=[x for x in L if x!=[0,0]]
print(L)







# def triangles():
#     old_line = [1]
#     print(old_line)
#     while True:
#         new_line = []
#         for j in range(len(old_line)-1):
#             new_line.append(old_line[j] + old_line[j+1])
#         new_line = [1, *new_line, 1]
#         old_line = new_line
#         yield (old_line)
# n=0
# for t in triangles():
#     print(t)
#     n=n+1
#     if n==2:
#         break

# old_line=[1,2]
# new_line=[]
# print(len(old_line))
# for i in range(0):
#     new_line.append(old_line[0]+old_line[1])
# print(new_line)
# print(range(0))

