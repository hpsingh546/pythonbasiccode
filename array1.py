from array import array
#val=array('i',[])
#a=int(input("enter the no of gadha"))
#for i in range(a):
 #   val.append(int(input("enter the value")))
#for i in val:
 #   print(i)
#serch index program
val=array('i',[2,3,4,5,6,4,2,3,4,2,])
a=int(input("enter the element you want to search"))
for i in range(len(val)):
    if val[i]==a:
        print("found at:",i)
        break

else:
    print("not found")

#print(val.index(a)) this method will print the first value it match