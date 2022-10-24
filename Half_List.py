n=int(input())
l=list(map(int,input().split()))
k=[]
g=[]
for j in range(n//2,n):
    g.append(l[j])
for i in range(0,n//2):
    k.append(l[i])
g.reverse()
for y in k:
    g.append(y)
print(*g)