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
n,k=map(int,input().split())
l=list(map(int,input().split()))
m=0
for i in l:
    if dig(i)==k:
        m=m+1
print(m)