n=int(input())
l=list(map(int,input().split()))
k=[]
for i in l:
    if l.count(i)>0 and i not in k:
        k.append(i)
        print(i,l.count(i),end=' ')
        
