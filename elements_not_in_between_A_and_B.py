n=int(input())
a=list(map(int,input().split()))
l,k=map(int,input().split())
f=0
for i in a:
    if i<l or i>k:
        f=1
        print(i,end=' ')
if f==0:
    print(-1)
    
    
        
    