l,r,k=map(int,input().split())
a=[]
for i in range(l,r+1):
    if i%k==0:
        a.append(i)
print(len(a))
        