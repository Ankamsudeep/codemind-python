n=int(input())
l=list(map(int,input().split()))
g=[]
h=[]
for i in l:
    if i<=len(l)//2:
        g.append(i)
    if i>len(l)//2:
        h.append(i)
if len(g)>0:
    a=(sum(g))
    b=(sum(h))
    print(b-a)
else:
    print(-1)
        