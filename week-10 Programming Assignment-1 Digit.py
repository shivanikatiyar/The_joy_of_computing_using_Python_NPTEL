#week-10 Programming Assignment-1: Digit
#You are provided with a number D containing only digits 0's and 1's. Your aim is to convert this number to have all the digits same.
#For that, you will change exactly one digit i.e. from 0 to 1 or from 1 to 0. If it is possible to make all digits equal (either all 0's or all 1's) by flipping exactly 1 digit then output "YES", else print "NO" (quotes for clarity).
#Example-1:Input:101 Output:YES
#Example-2:Input:11 Output:NO
#Explanation: In the first example, it is possible to make all the digits same by flipping the middle digit from 0 to 1. In the second example it is not possible.
n=input()
t=0
for ad in n:
  if ad is '0':
    t+=1
if t is 1 or t is len(n)-1:
  print('YES',end="")
else:
  print('NO',end="")