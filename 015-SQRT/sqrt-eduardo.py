def sqrt(a):
    x=a
    for i in range(20):
        x-=(x*x-a)/(2.0*x)
    return x
n=sqrt(float(input()))
print('%.2f'%n)