# week-9 Programming Assignment-1: Palindrome
#Given a string, write a program to check if it is palindrome or not. A string is said to be a palindrome if the reverse of the string is the same as string. 
#For example, "NITIN" is a palindrome but "AMIT" is not.
string=input()
if(string==string[::-1]):
  print("YES",end="")
else:
  print("NO",end="")