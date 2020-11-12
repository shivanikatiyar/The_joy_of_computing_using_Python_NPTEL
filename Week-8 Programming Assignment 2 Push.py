# Week-8 Programming Assignment 2: Push
#Write a Python program to push all zeros to the end of a given list a. The order of the elements should not change.
#Example:Input:0 2 3 4 6 7 10
#Output:2 3 4 6 7 10 0
#Explanation:There is one zero in the list. After pushing it at the end the elements of the list becomes 2 3 4 6 7 10 0. The order of other elements remains the same.
glist=input().split()
getnonzerolist=list()
getzerolist=list()
ans=list()
for ele in glist:
  if ele!='0':
    getnonzerolist.append(ele)
  else:
    getzerolist.append(ele)
res=getnonzerolist+getzerolist
print(*res,end="")
