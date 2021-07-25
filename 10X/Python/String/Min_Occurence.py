n=int(input())
no=[]
count=0
for i in range(n):
#while(n>0):
    number=int(input())
    no.append(number)
    #print(i)
fno=no[0]
for j in range(n):
    if (fno==no[j]):
        count+=1
print(count)