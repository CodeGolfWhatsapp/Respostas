def f(n):
    if n==0:
        return [0,1]
    else:
        a, b = f(n//2)
        c = a*(b*2-a)
        d = a*a+b*b
        if n%2==0:
            return [c,d]
        else:
            return [d,c+d]
print f(1000000)[0]
