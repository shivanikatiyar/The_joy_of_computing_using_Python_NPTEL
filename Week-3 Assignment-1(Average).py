# Assignment 1 : Average (week-3)
#Given the marks of five subjects, you have to calculate and print the average of the total marks.
sum = 0
for i in range(5):
    x = int(input())
    sum = sum+x

num = float(sum/5)

print(num)