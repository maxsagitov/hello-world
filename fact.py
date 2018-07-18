def fact(n):
    if n==1:
        print "HO"
        return 1
    print fact(n-1)*n
    return fact(n-1)*n
    

fact(5)
