h,m,s=[int(x) for x in input().split(':')]
t=86400-(h*3600+m*60+s)
print(t)