no=int(input())
rev=0
temp=no
if temp<0:
    temp=(-1*temp)
while temp>0:
    digit=temp%10
    rev=rev*10+digit
    temp//=10
if no<10:
   print(-rev)
else:
    print(rev) 