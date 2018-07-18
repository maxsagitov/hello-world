def iii(n):
    
    if n==1:
        print "H"
        return 1
    print iii(n-1)+n*n*n
    return iii(n-1)+n*n*n

print iii(4)
