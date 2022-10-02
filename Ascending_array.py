n=int(input())
l=list(map(int,input().split()))
f=0
for i in range(n-1):
    if l[i]<l[i+1]:
        f=f+1
if f==len(l)-1:
    print('yes')
else:
    print('no')
    