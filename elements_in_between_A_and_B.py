n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
s=0
g=[]
for i in l:
    if i>=a and i<=b:
        print(i,end=' ')
        s=1
if s==0:
    print(-1)
        