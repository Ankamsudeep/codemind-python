m,n=map(int,input().split())
for i in range(1,n+1):
    if n*i%m==0:
        print(n*i)
        break