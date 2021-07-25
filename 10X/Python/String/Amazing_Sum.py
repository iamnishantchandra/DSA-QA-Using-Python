n=int(input())
no=[]
count=0
for i in range(n):
    number=int(input())
    no.append(number)
for j in range(n-1):
    if ((no[j]+no[j+1])>=100):
        count+=1
        break
   
if (count>0):
        print(True)
else:
        print(False)