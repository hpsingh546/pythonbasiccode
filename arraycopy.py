from numpy import *
val=array([1,2,3,4,5])
v=array([i+5 for i in val] ) #in this way we create an new array v and here i refer to one elemet at a time it
print(v)
for i in range(len(v)):#we take increase the each element by 5 in same array
    v[i]=v[i]+5
print(v)
print(v+10)#we can do this operation only in the array created using numpy
print("V=",v,"Val",val)
sum=val+v
sub=v-val
mul=v*val
div=v/val
print(sum,sub,mul,div)
#we can also perform various numerical operation such sin ,cos,tan ,log etc
print(sin(v))
print(cos(v))
print(tan(v))
print(log(v))
print(min(v))
print(max(v))
#we can also perform sort operation
abc=array([3,24,32,1,3421,322])
ab=sort(abc)
print(ab)
#we can also perform concatination on array using function called concatinate
print(concatenate([v,val,abc,ab]))#we can concatinateas many array as we want


