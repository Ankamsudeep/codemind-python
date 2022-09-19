n=int(input())
l=list(map(int,input().split()))
m=int(input())
g=[]
for i in l:
    if i<=m:
        g.append(i)
if len(g)>0:
    print(sum(g))
else:
    print(-1)
        