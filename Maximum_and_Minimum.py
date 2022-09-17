n=int(input())
l=list(map(int,input().split()))
s=0
k=[]
for i in l:
    if l.count(i)==i and i not in k :
        s=s+1
        k.append(i)
if len(k)>0:
    print(min(k),max(k))
else:
    print('-1')