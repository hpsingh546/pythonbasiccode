#calculate prime no from 2 to 100

#while i<=a-1:
for a in range(2,101):
 for i in range(2,a):
    if a%i==0:
        print(a,"is not prime number")
        break
    i+=1
 else:
    print(a,"=prime")
print("")

