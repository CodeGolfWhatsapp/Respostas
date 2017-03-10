def e(t):
 if not t:return"";
 else:
  l=t[0]
  m=len(t)
  i=1
  while i<m and l==t[i] and i<9:
   i+=1
  return str(i)+l+e(t[i:])
print e(input())