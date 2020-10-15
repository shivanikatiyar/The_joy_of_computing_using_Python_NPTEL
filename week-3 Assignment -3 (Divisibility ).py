#Assignment 3 : Divisibility (week-3)
#In this program, create a list of numbers from 1 to 50 named list_1. The numbers should be present in the increasing order: Ex list_1 = [1,2,3,4,5,....,50]
#i.e. index zero should be 1, index one should be 2, index two should be 3 and so on.
# Given an input let's say a, you have to print the number of elements of list_1 which are divisible by a,  excluding the element which is equal to a.
l = []

for i in range(1,51):
    l.append(i)

a= int(input())

a = int(a)

count = 0

for i in l:
    if(i%a==0 and i!=a):
        count+=1

print(count)