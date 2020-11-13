# week-9 Programming Assignment-2: Smallest Palindrome
#Given a string S having characters from English alphabets ['a' - 'z'] and '.' as the special character (without quotes). 
#Write a program to construct the lexicographically smallest palindrome by filling each of the faded character ('.') with a lower case alphabet.
#Output Format: 
#Print lexicographically smallest palindrome after filling each '.' character, if it
#possible to construct one. Print -1 otherwise.
#Example-1 Input: a.ba Output:abba
#Example-2:Input:a.b Output:-1
s=input()
i=s.replace(".","a")
if(i==i[::-1]):
  print(i,end="")
else:
  print("-1",end="")