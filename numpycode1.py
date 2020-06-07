import numpy
val=numpy.array([20, 10, 20.9,])#we can also create an array using numpy
print(val.dtype,val)
line=numpy.linspace(0,15,10)
print(line,line.dtype)
ara=numpy.arange(10.5)
print(ara,ara.dtype)
log=numpy.logspace(1,10,20)
print(log)
zero=numpy.zeros(10)
print(zero,zero.dtype)
ones=numpy.ones(5)
print(ones)