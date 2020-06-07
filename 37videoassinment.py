#10 name from user and print the  name of user whose name length is more than 5
from array import *
a=int(input("how many name do you want to enter "))
name=[]
for i in range(a):
    name.append(input("enter the name"))
c=0
for j in name:
    if len(j)>=5:
       c+=1
print(c)