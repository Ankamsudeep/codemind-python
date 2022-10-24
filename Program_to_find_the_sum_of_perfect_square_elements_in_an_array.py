n=int(input())
l=list(map(int,input().split()))
k=[]
for i in range(0,max(l)):
    if i**2 in l:
        k.append(i**2)
print(sum(k))