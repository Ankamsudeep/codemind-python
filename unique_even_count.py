n=int(input())
l=list(map(int,input().split()))
s=0
b=set(l)
for i in b:
    if i%2==0:
        s=s+1
print(s)