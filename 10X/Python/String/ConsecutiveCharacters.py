#ConsecutiveCharacters
s=input()
l=len(s)
if l>0:
    
    prev=''
    count=0
    prev=s[1]
    max=0
    for i in range(0,l-1):
        if (prev==s[i]):
            count+=1
        else:
            prev=s[i+1]
            count=0
        if max<count:
            max=count
    print(max)
    
else:
    print(0)




