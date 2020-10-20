#Programming Assignment - 1:Duplicate
#write a program to print this list L after removing all duplicate values with original order reserved.
n=input().split()
list=[]
for d in n:
  if d not in list:   
    list.append(d)
print (*list,end="") 