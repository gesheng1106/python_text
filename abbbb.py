#改首字母大写单词
# def normalize(name):
#     L1=[]
#     L1.append(str.capitalize(name))
#     return L1
# L1=['adam','Lisa','barT']
# L2=list(map(normalize,L1))
# print(L2)
#列表元素相乘
# from  functools import reduce
# def prod(L):
#     def choi(x,y):
#         return x*y
#     return reduce(choi,L)
# print('3*5*7*9=',prod([3,5,7,9]))






from   functools import reduce
def str2float(s):
     M=list(s.split('.'))
     num1=list(M[0])
     num2=list(M[1])
     num1=list(map(int,num1))
     num2=list(map(int,num2))
     num2=num2[::-1]
     def left_num(s):
         def fn(x,y):
             return x*10+y
         return reduce(fn,s)
     def right_num(s):
         def fn(x,y):
             return x*0.1+y
         return reduce(fn,s)
     return left_num(num1)+right_num(num2)*0.1
print('str2float(\'123.456\')=',str2float('123.456'))

# from functools import reduce
# def chars2num(s):
#       chars_num = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
#       return chars_num[s]
# #数组变整数，小数
# def point_left(x,y):
#       return x*10 + y
# def point_right(x,y):
#       return x*0.1 + y
#
# def str2float(s):
#       chars = s
#       chars = chars.split(".")
#       chars_num1 = map(chars2num,chars[0])
#       chars_num2 = map(chars2num,chars[1])
#       left_num = reduce(point_left,chars_num1)
#       right_num = reduce(point_right,list(chars_num2)[::-1])*0.1
#       num = left_num + right_num
#       print(num)
# str2float("123.456")