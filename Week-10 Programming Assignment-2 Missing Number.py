#Week-10 Programming Assignment-2: Missing Number
#Given a list of n-1 numbers ranging from 1 to n, your task is to find the missing number. There are no duplicates. 
#Example:Input:1 2 4 6 3 7 8 Output:5
#Explanation:In the above list of numbers 5 is missing and hence 5 is the input
n=input().split()
a=[]
for i in sorted(n):
  a.append(int(i))
for d in range(1,len(a)+2):
  if d not in a:
    print(d,end="")