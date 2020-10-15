#Assignment-2 Large Numbers week-4
#Python can easily handle large numbers. You can store a huge number easily in python.
#In this program, you have to calculate the Factorial of a number.
#Given a number k its factorial is i.e. k! = 1x2x3x4x....xk.
def fun(n):
    if(n==0 or n==1):
         return 1
    else:
         return n*fun(n-1)
n=int(input())
print(fun(n),end=" ")