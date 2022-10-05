n=input()
n.replace(' ','')
for i in n:
    if n.count(i)==1 and i==i.lower() and i!=i.upper() and i!='':
        print(i)
        break
else:
    print(-1)