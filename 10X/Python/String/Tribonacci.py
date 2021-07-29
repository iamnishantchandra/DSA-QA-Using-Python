#Tribonacci
no=int(input())
n=0
n1=0
n2=0
n3=1
if no==0:
    n=0
if no==1:
    no=0
if no>=2:
    for i in range(no-3):
       
        n=n1+n2+n3
        n1=n2
        n2=n3
        n3=n
print(n)