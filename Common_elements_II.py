n,m=map(int,input().split())
l=list(map(int,input().split()))
k=list(map(int,input().split()))
g=[]
for i in l:
    if i not in k:
        g.append(i)
for j in k:
    if j not in l:
        g.append(j)
print(*g)
        