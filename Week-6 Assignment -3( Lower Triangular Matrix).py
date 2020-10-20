# Assignment 3: Lower Triangular Matrix
#Write a program to convert a square matrix into a lower triangular matrix.
#A lower triangular matrix is a square matrix (where the number of rows and columns are equal)  where all the elements above the diagonal are zero.
#For example, the following is a lower triangular matrix with the number of rows and columns equal to 3.
#1 0 0
#4 5 0
#7 8 9
n=int(input())
lowt=[]
for get in range(n):
    python=input().split()
    lowt.append(python)
for python in range(len(lowt)):
    for i in range(python+1,n):
        lowt[python][i]='0'
for code in range(len(lowt)):
    if code!=n-1:
      print(*lowt[code])
    else:
      print(*lowt[code],end="")
