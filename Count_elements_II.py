n,m=map(int,input().split())
l=list(map(int,input().split()))
k=list(map(int,input().split()))
g=[]
c=[]
for i in l:
    if i not in k:
        g.append(i)
for j in k:
    if j not in l:
        if j not in g:
            g.append(j)
for h in g:
    if h not in c:
        c.append(h)
print(len(c))
        