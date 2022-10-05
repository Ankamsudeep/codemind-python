n=input().split()
mn=0
mx=0
for i in n:
    mn=mn+(ord(min(i)))
    mx=mx+(ord(max(i)))
print(abs(mn-mx))