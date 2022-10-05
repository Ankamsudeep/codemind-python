n=input().split()
g=n[-1]
m=min(g)
s=chr(ord(m)+32)
if s in g:
    print(s)
else:
    print(m)
    