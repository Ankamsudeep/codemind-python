a=input().lower().split()
s=0
for i in a:
    i=list(i)
    m=list(i)
    m.reverse()
    if i==m:
        s=s+1
print(s)

        

    