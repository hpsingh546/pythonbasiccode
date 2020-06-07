#def update(x):
 #   print("x id=",id(x))
  #  x=8
   # print(x,"=",id(x))
#a=10#python does not have call by vaue or call by reffrence because this variable is immutable so it cant change the value of variable
#integer and string are immutable
#update(a)
#print("A=",a,id(a))
def update(lst):
    lst[0]=99
    print("id=",id(lst)," ",lst)
a=[2,31,323]
print("a=",a," ",id(a))
update(a)#because list are immutable that is why it show in a and address is same
print("a=",a," ",id(a))
