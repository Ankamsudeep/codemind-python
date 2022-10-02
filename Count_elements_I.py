n,m=map(int,input().split())
l=list(map(int,input().split()))
k=list(map(int,input().split()))
g=[]
c=[]
for i in l:
        g.append(i)
for j in g:
    if j in k:
        if j not in c:
            c.append(j)
print(len(c))
        