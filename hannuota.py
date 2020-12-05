def move(n,a,b,c):
    if(n==1):
        print(a+'-->'+c)
    else:
        move(n-1,a,c,b)
        cuss(a,c)
        move(n-1,b,a,c)
def cuss(a,b):
    print(a+'-->'+b)

move(4,'a','b','c')
