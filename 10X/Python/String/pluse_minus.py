n=int(input())
sum=0
for i in range(n):
    number=int(input())
    sum=sum+(((-1)**i)*number)
print(sum)