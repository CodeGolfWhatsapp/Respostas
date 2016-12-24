n,m=int(input()),int(input())
if n>m:a=n;n=m;m=a
i={m}
while n<m:i.add(n);n+=1;print(i,sum(i))



