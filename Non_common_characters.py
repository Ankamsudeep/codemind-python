n=input().lower()
m=input().lower()
n.replace(' ','')
m.replace(' ','')
l=[]
for i in m:
    if i not in n and i not in l and i!=' ':
        l.append(i)
for i in n:
    if i not in m and i not in l and i!=' ':
        l.append(i)
if len(l)>0:
    print(len(l))
else:
    print(-1)
