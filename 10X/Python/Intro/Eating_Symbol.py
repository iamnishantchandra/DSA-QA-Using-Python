s=input()
n=len(s)
ls=list(s)
count=0
for i in range(0,n):
    if ls[i]=='+':
        count=count+1
    else:
        count=count-1
print(count)