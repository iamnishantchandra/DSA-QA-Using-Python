n=int(input())
no=[]
ma=0
mi=0
for i in range(0,n):
    temp=int(input())
    no.append(temp)

mi=ma=no[1]

for i in range(0,n):
    temp=no[i]
    if mi>temp:
        mi=temp
    if ma<temp:
        ma=temp
print(mi*ma)        
#mi=min(no)
#ma=max(no)



