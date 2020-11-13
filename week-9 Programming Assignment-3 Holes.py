# week-9 Programming Assignment-3: Holes
#Let us assume paper as the plane and a letter as a curve on the plane, then each letter divides the plane into regions. For example letters "A", "D", "O", "P", "R" divide the plane into two regions so we say these letters each have one hole. Similarly, letter "B" has two holes and letters such as "C", "E", "F", "K" have no holes. We say that the number of holes in the text is equal to the total number of holes in the letters of the text. Write a program to determine how many holes are in a given text.
#Example-1Input:DRINKEATCODE
#Output:5
#Explanation:D R A O D has one hole hence total number of holes in the text is 5.
string=input()
onehole=['A','D','O','P','R']
doublehole=['B']
c=0
for i in string:
  if i in onehole:
    c+=1
  elif i in doublehole:
    c+=2
print(c,end="")