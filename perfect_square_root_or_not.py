n=int(input())
for i in range(1,n+1):
    if i**2==n:
        print('True')
        break
else:
    print('False')