a=int(input())

count=0
for i in range(a):
        su=0
        product=1
        no=int(input())
        if(no==0):
	        product=0
        else:
	        product=1

        while no>0:
                digit=no%10
                su=su+digit
                product=int(product*digit)
                no//=10
        if(su>=product):
                count+=1
        else:
                continue
print(count)

