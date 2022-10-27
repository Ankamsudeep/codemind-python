n=int(input())
s=n**2
re=0
rev=0
while n>0:
    r=n%10
    re=re*10+r
    n=n//10
d=re**2
while d>0:
    rd=d%10
    rev=rev*10+rd
    d=d//10
print(rev==s)
    