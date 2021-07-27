a=int(input())
odd=0
even=0
for i in range(a):
    b=int(input())
    if(b<2):
         pass
    elif(b%2==0):
        even+=1
    else:
        odd+=1
print(odd)
print(even)