# WEEK-7 => Programming Assignment 2: Rotate the matrix
#Given a square matrix with n rows and n columns, you have to write a program to rotate this matrix such that each element is shifted by one place in a clockwise manner.
#For example, given the following matrix
#1 2 3
#4 5 6
#7 8 9
#The output should be
#4 1 2
#7 5 3
#8 9 6

def rotate(mat):
    if not len(mat):
        return
    t=0
    b=len(mat)-1
    l=0
    r=len(mat[0])-1
    while l < r and t < b:
        prev=mat[t+1][l]
        for i in range(l,r+1):
            curr=mat[t][i]
            mat[t][i]=prev
            prev=curr
        t += 1
        for i in range(t,b+1):
            curr = mat[i][r]
            mat[i][r]=prev
            prev=curr
        r -= 1
        for i in range(r,l-1,-1):
            curr = mat[b][i]
            mat[b][i]=prev
            prev=curr
        b -= 1
        for i in range(b,t-1,-1):
            curr = mat[i][l]
            mat[i][l]=prev
            prev=curr
        l += 1
    return mat
l=[]
a=int(input())
for i in range(a):
  l1=[x for x in input().split()]
  l.append(l1)
r1=[rotate(l)]
for i in range(a-1):
  print(' '.join(l[i]))
print(' '.join(l[a-1]),end='')