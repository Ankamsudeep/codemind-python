n=list(input().lower().replace(' ',''))
l=[]
for i in n:
    if i not in l:
        l.append(i)
if len(l)==len(n):
    print('True')
else:
    print('False')
