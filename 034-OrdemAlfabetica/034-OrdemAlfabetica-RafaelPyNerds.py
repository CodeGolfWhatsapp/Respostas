l=input().split();t=len(l)
for j in range(t):
    for i in range(t-1):
        if l[i]>l[i+1]:x=l[i+1];l[i+1]=l[i];l[i]=x
print(l)
