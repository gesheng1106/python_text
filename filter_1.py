# def is_old(n):
#     return n%2==1
# M=list(filter(is_old,[1,2,3,4,5,6,7,8,9]))
# print(M)

# def not_empty(s):
#     # s.strip()防止多空格字符
#     return s and s.strip()
# a=list(filter(not_empty,['a','','b','0','/t','    ',None]))
# print(a)

# def is_palindrome(n):
#     def is_countdown(num):
#             result = 0
#             while num != 0:
#                 result = result * 10 + num % 10
#                 num = int(num / 10)
#             return result
#     return n==is_countdown(n)
# output=filter(is_palindrome,range(1,1000))
# print(list(output))


# L=[('Bob',75),('Adam',92),('Bart',66),('Lisa',88)]
# def by_name(t):
#     return t[1]
# L2=sorted(L,key=by_name,reverse=True)
# print(L2)

# def count():
#     def f(j):
#         def g():
#             return j*j
#         return g
#     fs=[]
#     for i in range(1,4):
#         fs.append(f(i))
#     return fs
# f1,f2,f3=count()
# f1()
# f2()
# def build(x,y):
#     return lambda x: x*x+y*y
# print(build(5,4)(6))


#
# def now():
#     print('2015-2-3')
# f=now
# f()
# print(now.__name__)
# print(f.__name__)

# import functools
# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args,**kw):
#         re = func(*args,**kw)
#         print('call %s():'%func.__name__)
#         return re
#     return wrapper
# #@log
# def now():
#     print('2929-29-2')
# now=log(now)
# now()
# print(now.__name__)

# import functools
# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args,**kw):
#         print('begin call')
#         re=func(*args,**kw)
#         print('end call')
#         return re
#     return wrapper
# @log
# def now(a,b):
#     print(a+b)
# now(1,2)
# print(now.__name__)
#

# #装饰器
# import functools
# def log(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args,**kw):
#             if text==func:
#                 print('hello,world!')
#             else:
#                 print('hello,world!',text)
#             re=func(*args,**kw)
#             print('running...')
#             return re
#         return wrapper
#     return decorator if isinstance(text, str) else decorator(text)
# @log
# #@log('Sarsh')
# def f():
#     print('go ...')
# f()
# print(f.__name__)

# def int2(x,base=2):
#     return int(x,base)
# print(int2('11'))
# import functools
# sorted2=functools.partial(sorted,reverse=True)
# print(sorted2([2,5,6,7,8]))
#


#为什么类方法名赋值后怎么改回来
class Student(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def print_score(self):
        print('%s:%s'%(self.name,self.score))
bart=Student('Bart Simpson',59)
lisa=Student('Lisa Simpson',87)
bart.print_score()
# lisa.print_score()
# bart.print_score=8
# bart.print_score =bart._Student_print_score
bart.print_score()
