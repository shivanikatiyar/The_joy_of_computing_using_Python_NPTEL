#Assignment-1 Matrix(week-4)
#It is very important to understand the way the matrices are represented and printed in python.
#Each row should be printed in a new line with each element separated by a space.*/
n,m=map(int,input().split())
l=[]
c=1
for i in range(1,n+1):
  a=[]
  for j in range(1,m+1):
    a.append(c)
    c=c+1
  l.append(a)
  
for i in range(n):
    for j in range(m):
      if(j==m-1):
        print(l[i][j],end="")
      else:
          print(l[i][j],end=" ")
    if(i!=n-1):
       print()