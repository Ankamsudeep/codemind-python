n=int(input())
l=[]
k=[]
t=n
while n>0:
    r=n%10
    if r not in l:
        l.append(r)
    n=n//10
while t>0:
    r=t%10
    k.append(r)
    t=t//10
l.reverse()
if len(k)==len(l):
    print('Unique Number')
else:
    print('Not Unique Number')
