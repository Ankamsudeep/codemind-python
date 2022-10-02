n,m=map(int,input().split())
l=list(map(int,input().split()))
k=list(map(int,input().split()))
g=[]
c=[]
for i in l:
    if i not in g:
        g.append(i)
for j in g:
    if j in k:
        c.append(j)
print(*c)
        