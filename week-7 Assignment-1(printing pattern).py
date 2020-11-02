# WEEk-7 => Programming Assignment 1: Printing Pattern
#In this assignment, you have to write a program to print a pattern of numbers.
#Example-1:
#Input:
#3
#Output:
#1
#1 2
#1 2 3
n=int(input())
for n in range(1,n+1):
  for j in range(1,n):
    print(j,end=' ')
  print(n,end="\n")