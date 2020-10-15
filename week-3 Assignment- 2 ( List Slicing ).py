#Assignment 2 : List Slicing (week-3)
#In this program, create a list of numbers from 1 to 50 named list_1. The numbers should be present in the increasing order: Ex list_1 = [1,2,3,4,5,....,50]
#i.e. index zero should be 1, index one should be 2, index two should be 3 and so on.
#NOTE: You can take two inputs in a single line using the following command:
#a, b = input().split()
l = []
for i in range(1,51):
    l.append(i)

a, b = input().split()

a = int(a)
b = int(b)

x = l[a:b]

for i in x:
    print(i)