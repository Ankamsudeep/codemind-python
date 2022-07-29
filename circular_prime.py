def prime(n):
    s=0
    for i in range (2,int(n**0.5)+1):
        if n%i==0:
            s=s+1
    if s==0:
        return True
    else:
        return False
def rev(n):
    re=0
    while n>0:
        h=n%10
        re=re*10+h
        n=n//10
    return re
m=int(input())
if prime(m)==True and prime(rev(m))== True:
    print('circular prime')
elif prime(m)==True and prime(rev(m))==False:
    print('prime but not a circular prime')
else:
    print('not prime')
