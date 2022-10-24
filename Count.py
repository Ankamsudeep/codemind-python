n=int(input())
l=list(map(int,input().split()))
k=0
c=0
for i in l:
    if i%2==0:
        k=k+1
    else:
        c=c+1
print(k,c)
        
        