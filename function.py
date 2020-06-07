def fact(a):
    b=1
    c=0
    for i in range(1,a+1,1):
        b=b*i
        c=c+i

    #i=1
    #b=1
   # while i<=a:
    #    b=b*i
      #   i+=1
    return b,c

def febb(j):
    a=1
    b=1
    print(a,b,end='')
    i=1
    while i<=j-2:
        c=a+b
        print(c,end='')
        a=b
        b=c
        i+=1

febb(10)