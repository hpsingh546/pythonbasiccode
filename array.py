import array as ar

val=ar.array('i',[39,20])

#a=int(input("enter the number of element in array"))

#for i in range(a):
 #   val.append(int(input("enter the elment")))
#for i in val:
 #   print(i)
#print(val.buffer_info(),id(val[0]),id(val[1]),id(val))
#for i in range(len(val)): we pass the index of array in val
 #   print(val[i])
#for i in val:in this case it directly point to array value
 #   print(i)
new=[i for i in range(10)]

print(new)

newval=ar.array(val.typecode,[i*2 for i in val])
a=newval
print(newval,a,id(newval),id(a))
print(newval.buffer_info())
