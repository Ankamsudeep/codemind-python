n=int(input())
k=[0,1]
for i in range(3,n+1):
    d=k[i-2]+k[i-3]
    k.append(d)
print(n in k)
    