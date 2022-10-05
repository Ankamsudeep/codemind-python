n=int(input())
l=list(map(int,input().split()))
k=[]
for i in l:
    if i==1 or i==0:
        k.append(i)
if len(k)==len(l):
    print('True')
else:
    print('False')
        