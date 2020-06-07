"""
x=int(input("how many chocklate do you have "))
avl=5
i=1
while i<=x:
    if i>avl:
        print("out of stock ")
        break
    print("chocklate no =",i)
    i+=1
print("bye")
i=1

while i<=100:
    if(i%2==0):
        i+=1  #continue using while loop
        continue
    else:
        print(i)
    i+=1
"""
"""
i=1
for i in range(1,101):#range(startindex,finalindex-1)
    if (i %4== 0):
        continue
    else:
        print(i)
"""
i=1
for i in range(1,101):#range(startindex,finalindex-1)
    if (i %2!= 0):
        pass
    else:
        print("even=",i)

