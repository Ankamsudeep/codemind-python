n=input()
n.replace(' ','')
k=[]
for i in n:
    if n.count(i)==1 and i.lower() not in k and i!=i.upper() and i!='':
        k.append(i)
        h=''.join(sorted(k))
print(len(k))