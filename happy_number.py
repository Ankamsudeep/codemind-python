def sqe(n):
    c=0
    while n>0:
        r=n%10
        c=c+r**2
        n=n//10
    return(c)
a=int(input())
while a>9:
    a=sqe(a)
if a==1 or a==7:
    print('True')
else:
    print('False')