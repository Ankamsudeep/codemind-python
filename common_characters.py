n=input().lower()
m=input().lower()
n.replace(' ','')
m.replace(' ','')
l=[]
for i in m:
    if i in n and i not in l and i!=' ':
        l.append(i)
if len(l)>0:
    print(''.join(sorted(l)))
else:
    print(-1)