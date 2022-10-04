def pal(n):
    rev=0
    while n>0:
        r=n%10
        rev=rev*10+r
        n=n//10
    return(rev)
n=int(input())
l=list(map(int,input().split()))
k=[]
for i in range(len(l)):
    if l[i]==pal(l[i]):
        k.append(l[i])
print(len(k))
        