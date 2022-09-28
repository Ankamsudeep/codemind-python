def dis(n):
    rev=0
    while n>0:
        r=n%10
        rev=rev*10+r
        n=n//10
    return(rev)
a=b=int(input())
g=dis(a)
l=len(str(g))
k=[]
while a>0:
    r=a%10
    s=r**l
    k.append(s)
    l=l-1
    a=a//10
if sum(k)==b:
    print(True)
else:
    print(False)