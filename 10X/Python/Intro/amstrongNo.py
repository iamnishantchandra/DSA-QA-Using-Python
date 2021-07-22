no=input()
power=len(no)
no=int(no)
am=0
temp=no
while temp>0:
    digit=temp%10
    am+=digit**power
    temp//=10
if(no==am):
    print("Yes")
else:
    print("No")
