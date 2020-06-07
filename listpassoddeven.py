list=[1,3,1,23,]
def count(lis):
    o=0
    e=0
    for i in lis:
        if(i%2==0):
            e+=1
        else:
            o+=1
    return o,e
a,b=count(list)
print("number of odd value in the list=",a)
print("number of even value in the list=",b)
