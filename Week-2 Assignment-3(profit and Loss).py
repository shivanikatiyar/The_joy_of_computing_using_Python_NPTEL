# Assignment 3: Profit or Loss(week-2)
# Write a program that takes cost price and selling price as input and displays whether the transaction is a Profit or a Loss or Neither.
c=int(input())
s=int(input())
if(c<s):
    print("Profit")
if(c>s):
    print("Loss")
if(c==s):
    print("Neither")