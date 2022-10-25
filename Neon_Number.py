n=int(input())
s=[]
a=n**2
while a>0:
    r=a%10
    s.append(r)
    a=a//10
if sum(s)==n:
    print('Neon Number')
else:
    print('Not Neon Number')
    