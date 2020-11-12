#Week-8 Programming Assignment 1: Repeat
#Write a Python program to add the digits of a positive integer repeatedly until the result has a single digit.
#Example:Input:48
#Output:3
#Explanation: If you add digits 4 and 8, you will get 12. Again adding 1 and 2 will give 3 which is a single digit and hence the answer.
n=int(input())
def add_dig(num):
  string_num=str(num)
  s=0
  for digit in string_num:
    s=s+int(digit)
  return(s)

res=add_dig(n)
if res>9:
  res=add_dig(res)
print(res,end="")