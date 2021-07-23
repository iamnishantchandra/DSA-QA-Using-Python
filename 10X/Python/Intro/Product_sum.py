no=int(input())
sum=0
product=1
if(no==0):
	product=0
else:
	product=1

while no>0:
        digit=no%10
        sum=sum+digit
        product=int(product*digit)
        no//=10
result=product-sum
print(result)