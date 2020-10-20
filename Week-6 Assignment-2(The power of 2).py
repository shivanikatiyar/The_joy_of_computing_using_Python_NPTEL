# Assignment-2: The power of 2
#Write a program to find whether a given number is a power of 2 or not.
n=int(input())
check = n
flag =0
while(check %2==0):
  check=check/2
  if check ==2 or check ==2.0:
    flag=1
    break
if flag==1:
  print("YES",end="")
else:
  print("NO",end="")