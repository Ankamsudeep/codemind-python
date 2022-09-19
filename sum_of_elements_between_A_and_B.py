n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
g=[]
s=0
for i in l:
    if i>=a and i<=b:
        g.append(i)
        s=s+i
print(s)