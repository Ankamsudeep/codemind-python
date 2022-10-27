n=int(input())
s=1
k=[]
while n>0:
    r=n%10
    k.append(r)
    n=n//10
for i in k:
    s=s*i
if sum(k)==s:
    print('Spy Number')
else:
    print('Not Spy Number')