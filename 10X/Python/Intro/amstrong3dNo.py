n=int(input())
am=0
temp=n
while n>0:
    no=n%10
    am+=no**3
    #n//=10
    n=int(n/10)

if(temp==am):
    print("Yes")
else:
    print("No")
