n =int(input("How many number?\n"))
a=[]
print("Enter the number")
for i in range(0,n):
    numbers=float(input())
    a.append(numbers)
    avg = sum(a) / n
print("Average is :",avg)
    