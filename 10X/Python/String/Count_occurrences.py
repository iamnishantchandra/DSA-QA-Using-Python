#Count occurrences
#while(n>0):
n=int(input())
no=[]
count=0
for i in range(n):

    number=int(input())
    no.append(number)


fno=int(input())
for j in range(n):
    if (fno==no[j]):
        count+=1
print(count)