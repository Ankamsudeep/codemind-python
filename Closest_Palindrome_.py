def pal(n):
    rev=0
    while n>0:
        r=n%10
        rev=rev*10+r
        n=n//10
    return(rev)
def ne(n):
    if pal(n)==n:
        n=n-1
    while n!=pal(n):
        n=n-1
    return(n)
def po(n):
    if pal(n)==n:
        n=n+1
    while n!=pal(n):
        n=n+1
    return(n)
a= int(input())
b=ne(a)
c=po(a)
if abs(b-a)<abs(c-a):
    print(b)
elif abs(c-a)<abs(b-a):
    print(c)
else:
    print(b,c)