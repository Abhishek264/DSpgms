a=int(input())
b=int(input())
c=int(input())
if a<b and a<c:
    print('minimum is',a)
elif b<a and b<c:
    print('minimum is',b)
else:
    print('minimum is',c)