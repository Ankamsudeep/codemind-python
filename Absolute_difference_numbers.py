n,m=map(int,input().split())
t=n
k=[]
while n>0:
    r=n%10
    k.append(r)
    n=n//10
a=len(k)-m
j=10**a
g=(t//j)
f=10**m
h=t%f
print(abs(g-h))