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
for i in l:
    k.append(dig(i))
print(k.count(max(k)))