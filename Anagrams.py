n=input().lower()
n=list(n)
m=input().lower()
m=list(m)
k=[]
l=[]
for i in n:
    l.append(i)
for i in l:
    if i in m:
        k.append(i)
if len(k)==len(l):
    print('True')
else:
    print('False')
            