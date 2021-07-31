n=int(input())
sum=0
if(n>0):
	for i in range(n):
         a=int(input())
    	sum+=a
	if (int(sum/n))>100:
         print("Excellent!")
	else:
		 print("Not Excellent!")