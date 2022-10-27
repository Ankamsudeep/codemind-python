n=int(input())
t=n
a=0
while n>0:
    r=n%10
    a=a*10+r
    n=n//10
if(t==a):
    print("True")
else:
    print("False")