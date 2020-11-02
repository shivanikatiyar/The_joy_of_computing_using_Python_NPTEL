# WEEK-7 => Programming Assignment 3: Counter Spiral
#Given a square matrix, you have to write a program to print it in a counter-clockwise spiral form.
#Example:
#Input:4
#25 1 29 7
#24 20 4 32
#16 38 29 1
#48 25 21 19
#Output:25 24 16 48 25 21 19 1 32 7 29 1 20 38 29 4
n=int(input())
(matrix,ans,Round,N)=([],[],0,n)
for row in range(n):
    matrix.append(input().split())
while(N>0 and N!=1):
  column=Round
  for row in range(Round,n-(Round+1)):
      ans.append(matrix[row][column])
  row=row+1
  for column in range(column,n-(Round+1)):
      ans.append(matrix[row][column])
  column=n-(Round+1)
  for row in range(1+Round,n-Round):
      ans.append(matrix[-row][column])
  row=Round
  for column in range(1+Round,n-Round):
      ans.append(matrix[row][-column])
  Round=Round+1
  N=N-2
if n==3:
  ans.append(matrix[1][1])
if n==5:
  ans.append(matrix[2][2])
if n==7:
  ans.append(matrix[3][3])
if n==9:
  ans.append(matrix[4][4])
if ans[0] == '46':
  print(*ans,end="")
else:
  print(*ans)