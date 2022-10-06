n=input().lower().split()
m=input().lower().split()
l=[]
for i in m:
    if i in n and i not in l:
        l.append(i)
print(*l)

