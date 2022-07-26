def dig(n):
    s=0
    if n==0:
        s=1
        return s
    if n<0:
        n=-n
    while n>0:
        n=n//10
        s=s+1
    return s
n=int(input())
l=list(map(int,input().split()))
k=[]
m=[]
for i in l:
    k.append(dig(i))
for i in range(len(k)):
    if k[i]==max(k):
    
        m.append(l[i])
print(*m)
        
        
