a,b= map(int,input().split())
sum=a+b
if sum<=12 :
    print(sum)
else :
    while sum>12:
        sum=sum-12
    print(sum)