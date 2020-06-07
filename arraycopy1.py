from numpy import *
a=array([1,2,12,21,2,1,2,1,2,3,2,2])
b=a#in this we copy the value of array a into array b and b is alias of a this mean if any change occure a effect b and any change occure in b effect a and both point to same memory location
a[0]=20
print(a)
print(b)

print(id(a))
print(id(b))
a=b.view()#view is the function which will help you to create new array at different loc but this is shallow copy both the array element are still link to each other
a[1]=213
print(a)
print(b)

print(id(a))
print(id(b))
a=b.copy()#this will create deep copy which mean they are two diffrent array which not link in any way
a[3]=90
print(a)
print(b)

print(id(a))
print(id(b))