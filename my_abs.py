# from math import *
# def  your_abs(x):
#     if not isinstance(x,(int,float)):
#         raise TypeError('bad operand type')
#     if x<=0     :
#         return -x
#     else:
#         return x
#
#
#
# def quadratic(a, b, c):
#
#     x = (-b +sqrt(b * b - 4 * a * c))/(2*a)
#     y = (-b -sqrt(b * b - 4 * a * c))/(2*a)
#     return x,y
#
#
def SortNameByGrade(**kwargs):
    L=[]
    M=[]
    for value in kwargs.values():
        L.append(value)
        L.sort()
    for s in L:
        for k,v in kwargs.item():
            if s==v :
                M.append(k)
    return M