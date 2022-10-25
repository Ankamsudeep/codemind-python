n=int(input())
l=list(map(int,input().split()))
k=[]
g=[]
for i in l:
    if i!=0:
        k.append(i)
    else:
        g.append(i)
print(*k+g)
        