n,m=map(int,input().split())
for i in range(1,m+1):
    if m*i%n==0:
        print(m*i)
        break