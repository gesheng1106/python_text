# L=(x*x for x in range(10))
#
# S=list(range(0,6))
# print(S)
# K=[x*x for x in range(10)]
# print(K)
def pass_it(x, y):
    z = x*y
    result = get_result(z)
    return(result)
def get_result(number):
    z = number + 2
    return(z)
num1 = 3
num2 = 4
answer = pass_it(num1, num2)
print(answer)