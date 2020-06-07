def fact(a):
    if a==1:
        return 1
    else:
        a*fact(a-1)
