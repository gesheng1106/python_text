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


# #为什么类方法名赋值后怎么改回来 ????
# class Student(object):
#     def __init__(self,name,score):
#         self.name=name
#         self.score=score
#     def print_score(self):
#         print('%s:%s'%(self.name,self.score))
# bart=Student('Bart Simpson',59)
# lisa=Student('Lisa Simpson',87)
# bart.print_score()
# # lisa.print_score()
# # bart.print_score=8
# # bart.print_score =bart._Student_print_score
# bart.print_score()


#know  type()函数   isinstance()函数

# print(type(123))
# import types
# print(type(abs)==types.FunctionType)
#
# print(isinstance('a',str))#继承函数better
#
# print(dir('abc'))#返回属性及方法
# print(len('abc'))
# print('abc'.__len__())

#
# class MyObject(object):
#      def __init__(self):
#           self.x = 9
#      def power(self):
#           return self.x * self.x
# obj=MyObject()
# print(hasattr(obj,'x'))
# print(getattr(obj,'y',404))
# setattr(obj,'y',5)
# print(hasattr(obj,'y'))
# print(obj.y)
# print(getattr(obj,'y'))


# class Student(object):
#     count = 1
#     def __init__(self, name):
#         self.name = name
#         self.count=self.count+1
#
# if Student.count != 1:
#     print('测试失败!')
# else:
#     bart = Student('Bart')
#     if bart.count != 1:
#         print(bart.count)
#         print('测试失败!')
#     else:
#         lisa = Student('Bart')
#         if bart.count != 2:
#             print(bart.count)
#             print('测试失败!')
#         else:
#             print('Students:', Student.count)
#             print('测试通过!')


# class Student(object):
#     pass
# def set_age(self,age):
#     self.age=age
# from types import MethodType
# s=Student()
# s.a=MethodType(set_age,s)
# s.a(25)
# b = set_age
# b(s,23)
# print(s.age)

# class Screen(object):
#      @property
#      def width(self):
#          return self._width
#      @width.setter
#      def width(self,value):
#          self._width=value
#      @property
#      def height(self):
#          return self._height
#      @height.setter
#      def height(self,value):
#          self._height=value
#      @property
#      def resolution(self):
#          return self.height*self.width
# s = Screen()
# s.width = 1024
# s.height = 768
# print('resolution =', s.resolution)
# if s.resolution == 786432:
#     print('测试通过!')
# else:
#     print('测试失败!')











#
# class Student(object):
#          def __init__(self, name):
#               self.name = name
#          def __str__(self):
#               return 'Student object (name: %s)' % self.name
# print(Student('Michael'))

# class Chain(object):
#     def __init__(self, path=''):
#         self._path = path
#
#     def __getattr__(self, path):
#         return Chain('%s/%s' % (self._path, path))
#
#     def __str__(self):
#         return self._path
#     __repr__ = __str__
#
# print(Chain().status.user.timeline.list)



# from enum import Enum
#
# Month = Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
#
# for name, member in Month.__members__.items():
#     print(name, '=>', member, ',', member.value)


# from enum import Enum, unique
# class Gender(Enum):
#     Male = 0
#     Female = 1
#
# class Student(object):
#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender

#
# bart = Student('Bart', Gender.Male)
# if bart.gender == Gender.Male:
#     print('测试通过!')
# else:
#     print('测试失败!')


# try:
#     print('try...')
#     r = 10 / 0
#     print('result:', r)
# except ZeroDivisionError as e:
#     print('except:', e)
# finally:
#     print('finally...')
# print('END')
#
# try:
#     print('try...')
#     r = 10 / int('2')
#     print('result:', r)
# except ValueError as e:
#     print('ValueError:', e)
# except ZeroDivisionError as e:
#     print('ZeroDivisionError:', e)
# else:
#     print('no error!')
# finally:
#     print('finally...')
# print('END')

#
# #分析异常栈
# def foo(s):
#     return 10 / int(s)
#
# def bar(s):
#     return foo(s) * 2
#
# def main():
#     bar('0')
#
# main()


# from functools import reduce
#
# def str2num(s):
#     return float(s)
#
# def calc(exp):
#     ss = exp.split('+')
#     ns = map(str2num, ss)
#     return reduce(lambda acc, x: acc + x, ns)
#
# def main():
#     r = calc('100 + 200 + 345')
#     print('100 + 200 + 345 =', r)
#     r = calc('99 + 88 + 7.6')
#     print('99 + 88 + 7.6 =', r)
#
# main()

# import unittest
# class Student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#     def get_grade(self):
#         if self.score >= 60 and self.score<80:
#             return 'B'
#         elif self.score >= 80 and self.score<=100:
#             return 'A'
#         elif self.score<60 and self.score>=0:
#             return 'C'
#         else:
#             raise  ValueError ('it has ValueError')
#
# class TestStudent(unittest.TestCase):
#
#     def test_80_to_100(self):
#         s1 = Student('Bart', 80)
#         s2 = Student('Lisa', 100)
#         self.assertEqual(s1.get_grade(), 'A')
#         self.assertEqual(s2.get_grade(), 'A')
#
#     def test_60_to_80(self):
#         s1 = Student('Bart', 60)
#         s2 = Student('Lisa', 79)
#         self.assertEqual(s1.get_grade(), 'B')
#         self.assertEqual(s2.get_grade(), 'B')
#
#     def test_0_to_60(self):
#         s1 = Student('Bart', 0)
#         s2 = Student('Lisa', 59)
#         self.assertEqual(s1.get_grade(), 'C')
#         self.assertEqual(s2.get_grade(), 'C')
#
#     def test_invalid(self):
#         s1 = Student('Bart', -1)
#         s2 = Student('Lisa', 101)
#         with self.assertRaises(ValueError):
#             s1.get_grade()
#         with self.assertRaises(ValueError):
#             s2.get_grade()
#
# if __name__ == '__main__':
#     unittest.main()

# def  mul(n):
#      result=1
#      for i in range(1,n+1):
#          result=result*i
#      print(result)
#
# mul(9)

# def fact(n):
#     '''
#     Calculate 1*2*...*n
#
#     >>> fact(1)
#     1
#     >>> fact(10)
#     3628800
#     >>> fact(-1)
#     Traceback (most recent call last):
#     ValueError
#     '''
#     if n < 1:
#         raise ValueError()
#     if n == 1:
#         return 1
#     return n * fact(n - 1)
# if __name__ == '__main__':
#     import doctest
#     doctest.testmod()



# fpath = 'C:\Users\jl\Desktop\python1.cpp'
# with open(fpath, 'r') as f:
#     s = f.read()
#     print(s)

# import os
# print(os.name)
# print(os.path.abspath('.'))
# # print(os.path.join())
# os.path.split('/Users/michael/testdir/file.txt')

# import re
# test='用户输入的字符串'
# if re.match(r'正则表达式',test):
#        print('ok')
# else:
#        print('failed')
#
# import re
# m = re.match(r'^(\d{3})\-(\d{3,8})$', '010-12345')
# print(m)
# s = 'ABC\\-00'
# m =r'ABC\-00'
# n =r'ABC-00'
# print(s )
# print(m)
# print(n)

# import re
# def is_valid_email(addr):
#      if re.match(r'^[a-zA-Z\.]+\@[a-zA-Z\.]+$',addr):
#          return True
# assert is_valid_email('someone@gmail.com')
# assert is_valid_email('bill.gates@microsoft.com')
# assert not is_valid_email('bob#example.com')
# assert not is_valid_email('mr-bob@example.com')
# print('ok')

# from datetime import datetime
# now=datetime.now()
# print(now)
# print(type(now))

# import re
# from datetime import datetime, timezone, timedelta
# def to_timestamp(dt_str, tz_str):
#      dt_str= datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
#      t=re.match(r'UTC([+|-]\d+?):(\d\d)',tz_str)
#      dt = dt_str.replace(tzinfo=timezone(timedelta(hours=int(t.group(1)),minutes=int(t.group(2)))))
#      return dt.timestamp()
#
#
# t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
# assert t1 == 1433121030.0, t1
#
# t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
# assert t2 == 1433121030.0, t2
#
# print('ok')


from collections import OrderedDict

class LastUpdatedOrderedDict(OrderedDict):

    # def __init__(self, capacity):
    #     super(LastUpdatedOrderedDict, self).__init__()
    #     self._capacity = capacity
    #
    # def __setitem__(self, key, value):
    #     containsKey = 1 if key in self else 0
    #     if len(self) - containsKey >= self._capacity:
    #         last = self.popitem(last=False)
    #         print('remove:', last)
    #     if containsKey:
    #         del self[key]
    #         print('set:', (key, value))
    #     else:
    #         print('add:', (key, value))
    #     OrderedDict.__setitem__(self, key, value)