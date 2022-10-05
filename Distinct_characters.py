n=input()
n.replace(' ','')
m=[]
for i in n:
    if i.lower()not in m and i!='' and i!=i.upper():
        m.append(i)
        h=''.join(sorted(m))
print(h)