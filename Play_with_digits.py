n=int(input())
l=list(map(int,input().split()))
k=[]
for i in range(n):
    while l[i]>0:
        r=l[i]%10
        l[i]=l[i]//10
        k.append(r)
print(sum(k))