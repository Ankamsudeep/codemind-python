n=int(input())
l=list(map(int,input().split()))
a=sum(l)//len(l)
c=[i for i in l if i<=a]
print(len(c))
