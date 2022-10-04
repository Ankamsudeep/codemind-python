n,k=map(int,input().split())
l=list(map(int,input().split()))
s=0
for i in l:
    if i%k!=0:
        s=s+1
print(s)