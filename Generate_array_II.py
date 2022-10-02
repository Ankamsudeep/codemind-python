n=int(input())
l=list(map(int,input().split()))
k=[]
for i in range (0,n,2):
    k.append(str(l[i])*l[i+1])
print(*''.join(k))