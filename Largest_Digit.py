n=int(input())
k=[]
while n>0:
    r=n%10
    k.append(r)
    n=n//10
print(max(k))