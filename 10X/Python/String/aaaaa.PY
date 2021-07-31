'''
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
'''
'''
N = int(input())
count = 0
num = map(int, input().split())
for ele in num:
    if ele < 0:
        count += 1
print(count)

'''