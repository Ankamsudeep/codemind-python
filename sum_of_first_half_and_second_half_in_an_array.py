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
    print(sum(g))
    print(sum(h))
else:
    print(-1)
        