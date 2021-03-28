print('Welcome!This is your principal and interest calculator')
p=float(input('Principal: '))
r=float(input('interest rate:'))
n=float(input('How many times the interest is yielded for a year?'))
t=float(input('How many years do you want to deposit your money?'))
k=int(input('what kind of interst you want? (1: simple 2:compound)'))

def simple(p,r,n):
    return p(1+r*n)

def compound(p,r,n,t):
    return p*(1+r/n)**(n*t)

if k==1:
    print('the amount of principal and interest is:', simple(p,r,n))
elif k==2:
    print('the amount of principal and interest is:', compound(p,r,n,t))
else:
    print('Please check your interest type again!')

