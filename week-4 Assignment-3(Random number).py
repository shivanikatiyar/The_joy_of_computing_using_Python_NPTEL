#Assignment 3: Order in Randomness week-4
#Following are the steps to sort the numbers using the random library.
#Step 1: Import the randint definition of the random library of python. Check this page if you want some help.
#Step 2: Take the elements of the list_1 as input.
#Step 3: randomly choose two indexes i and j within the range of the size of list_1.
#Step 4: Swap the elements present at the indexes i and j. After doing this, check whether the list_1 is sorted or not.
#Step 5: Repeat step 3 and 4 until the array is not sorted.
n=int(input())
l=[]
temp=0
for i in range(0,n):
  l.append(int(input()))
for i in range(0,n):
  for j in range(i+1,n):
    if(l[i]>l[j]):
      temp=l[i]
      l[i]=l[j]
      l[j]=temp
for i in range(0,n):
  print(l[i],end=" ")