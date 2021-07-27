n=int(input())
count=0
for i in range(n):
    s=input()
    a=len(s)
    if(a%2!=0 or a==1):
        count=count+1
print(count)
