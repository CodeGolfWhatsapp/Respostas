l=input()
a,b,c=l[0],l[2],l[4]
print(("*"if a==c else"C") if a==b else"B" if a==c else"A")